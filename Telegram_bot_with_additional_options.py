"""
                            Доработка телеграм бота для отслеживания сна.

    Доработаем свой код и добавим сохранение данных в файл.

        Так же нужно учесть, что данные должны не просто записываться в файл, а дополняться записями - для хранения
        всей историю наших заметок, а не только за 1 день.
"""

import telebot
import os
import json
from datetime import datetime

TOKEN = os.getenv("KEY")
bot = telebot.TeleBot(TOKEN)

# Файл для хранения данных
DATA_FILE = "sleep_data.json"


# Загрузка данных из файла
def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


# Сохранение данных в файл
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4, default=str)


# Загружаем данные при старте
data_sleep = load_data()

# Добавление кнопочной панели
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.row("/sleep", "/wake")
keyboard.row("/quality", "/notes")
keyboard.row("/stats", "/history")


# Обработчик команды /start
@bot.message_handler(commands=["start"])
def message_start(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я буду помогать тебе отслеживать параметры сна."
        "Нажми /sleep перед сном /wake утром.",
        reply_markup=keyboard
    )


# Обработчик команды /sleep
@bot.message_handler(commands=["sleep"])
def sleep_start(message):
    user_id = str(message.from_user.id)  # Преобразуем в строку для JSON
    current_time = datetime.now()

    # Инициализируем данные пользователя, если их нет
    if user_id not in data_sleep:
        data_sleep[user_id] = {"sleep_sessions": []}

    # Начало фиксации сна
    data_sleep[user_id]["current_session"] = {
        "start_time": current_time.isoformat(),
        "date": current_time.date().isoformat()
    }

    save_data(data_sleep)  # Сохраняем после изменения

    bot.send_message(
        message.chat.id,
        f"Твой сон начался {current_time.strftime("%H:%M")}. Спокойной ночи",
        reply_markup=keyboard
    )


# Обработчик команды /wake
@bot.message_handler(commands=["wake"])
def wake_up(message):
    user_id = str(message.from_user.id)
    print(f"DEBUG: Пользователь '{user_id}' вызывал функцию wake_up.")

    # Проверка наличия данных о начале сна
    if (user_id not in data_sleep or
            "current_session" not in data_sleep[user_id] or
            "start_time" not in data_sleep[user_id]["current_session"]):
        bot.send_message(
            message.chat.id,
            "Сначала нажми /sleep, чтобы зафиксировать начало сна.",
            reply_markup=keyboard
        )
        return

    end_time = datetime.now()
    start_time = datetime.fromisoformat(
        data_sleep[user_id]["current_session"]["start_time"]
    )
    duration = end_time - start_time

    # Вычисляем продолжительность сна в часах
    hours_slept = round(duration.total_seconds() / 3600, 2)

    # Сохраняем во временные данные
    data_sleep[user_id]["current_session"]["duration"] = hours_slept
    data_sleep[user_id]["current_session"]["end_time"] = end_time.isoformat()

    # Сохраняем после изменения
    save_data(data_sleep)
    print(f"DEBUG: Сессия сохранена, продолжительность сна: {hours_slept} часов.")

    # Создаём ответ для оценки качества
    force_reply = telebot.types.ForceReply(selective=True)

    # Предлагаем оценить качество сна
    msg = bot.send_message(
        message.chat.id,
        f"Твой сон длился {hours_slept} часов.\n"
        f" Оцени качество сна от 1 до 10: ",
        reply_markup=force_reply
    )

    # Регистрируем следующий щаг
    bot.register_next_step_handler(msg, quality_input)
    print("DEBUG: Обработчик для ввода данных о качестве сна зарегистрирован.")


# Сбор оценки качества сна
def quality_input(message):
    user_id = str(message.from_user.id)
    quality = message.text.strip()
    print(f"DEBUG: Функция quality_input. Пользователь поставил оценку о качестве сна: {quality}.")

    # Проверка корректности оценки
    if not quality.isdigit() or int(quality) < 1 or int(quality) > 10:
        print(f"DEBUG: Неверный ввод данных о качестве сна: {quality}.")
        force_reply = telebot.types.ForceReply(selective=True)
        msg = bot.send_message(
            message.chat.id,
            "Оценка должна быть число от 1 до 10. Попробуй снова.",
            reply_markup=force_reply
        )
        bot.register_next_step_handler(msg, quality_input)
        return

    # Сохраняем оценку во временные данные
    data_sleep[user_id]["current_session"]["quality"] = int(quality)
    save_data(data_sleep)
    print(
        f"DEBUG: Функция quality_input. Запись об оценке качества сна '{quality}' сохранена для пользователя {user_id}.")

    # Запрашиваем заметки о сне
    force_reply = telebot.types.ForceReply(selective=True)
    msg = bot.send_message(
        message.chat.id,
        "Опиши, пожалуйста, свой сон (например: спал(а) плохо, часто просыпался(лась)):",
        reply_markup=force_reply
    )
    bot.register_next_step_handler(msg, notes_input)


# Обработка заметок о сне и завершение сессии
def notes_input(message):
    user_id = str(message.from_user.id)
    notes = message.text.strip()
    print(f"DEBUG: Функция notes_input. Пользователь сделал заметку о сне: {notes}.")

    # Сохраняем заметки
    data_sleep[user_id]["current_session"]["notes"] = notes

    # Перемещаем текущую сессию в историю
    if "sleep_sessions" not in data_sleep[user_id]:
        data_sleep[user_id]["sleep_sessions"] = []

    data_sleep[user_id]["sleep_sessions"].append(
        data_sleep[user_id]["current_session"].copy()
    )

    # Очищаем текущую сессию
    del data_sleep[user_id]["current_session"]

    # Сохраняем после изменений
    save_data(data_sleep)
    print(f"DEBUG: Сессия завершена и сохранена в истории для пользователя: {user_id}.")

    bot.send_message(
        message.chat.id,
        "Спасибо! Данные о твоём сне сохранены. Хорошего дня!",
        reply_markup=keyboard
    )


# Обработчик команды /stats
@bot.message_handler(commands=["stats"])
def show_stats(message):
    user_id = str(message.from_user.id)

    if (user_id not in data_sleep or
            "sleep_sessions" not in data_sleep[user_id] or
            not data_sleep[user_id]["sleep_sessions"]):
        bot.send_message(
            message.chat.id,
            "У тебя пока нет записей о сне. Начни отслеживание с командой /sleep",
            reply_markup=keyboard
        )
        return

    sessions = data_sleep[user_id]["sleep_sessions"]

    # Рассчитываем статистику
    total_sessions = len(sessions)
    avg_duration = sum(session.get("duration", 0) for session in sessions) / total_sessions
    avg_quality = sum(session.get("quality", 0) for session in sessions) / total_sessions

    # Находим лучший и худший сон
    best_session = max(sessions, key=lambda x: x.get("quality", 0))
    worst_session = min(sessions, key=lambda x: x.get("quality", 10))

    stats_text = f"""
    Статистика твоего сна:

    • Всего записей: {total_sessions}.
    • Средняя продолжительность сна: {avg_duration:.2f}.
    • Среднее качество сна: {avg_quality:.1f}/10.

    • Лучший сон: {best_session.get("quality", "N/A")}/10.
      ({best_session.get("duration", "N/A")} часов.)

    • Худший сон: {worst_session.get("quality", "N/A")}/10.
      ({worst_session.get("duration", "N/A")} часов)
       """
    bot.send_message(
        message.chat.id,
        stats_text,
        reply_markup=keyboard
    )


# Обработчик команды /history
@bot.message_handler(commands=["history"])
def show_history(message):
    user_id = str(message.from_user.id)

    if (user_id not in data_sleep or
            "sleep_sessions" not in data_sleep[user_id] or
            not data_sleep[user_id]["sleep_sessions"]):
        bot.send_message(
            message.chat.id,
            "У тебя пока нет истории сна. Начни отслеживание с командой /sleep.",
            reply_markup=keyboard
        )
        return

    sessions = data_sleep[user_id]["sleep_sessions"][-10:]  # Последние 10 записей
    history_text = "История твоего сна (последние 10 записей):\n\n"

    for i, session in enumerate(reversed(sessions), 1):
        date = session.get("date", "Неизвестно")
        duration = session.get("duration", "N/A")
        quality = session.get("quality", "N/A")
        notes = session.get("notes", "Без заметок")

        if len(notes) > 50:  # Обрезаем длинные заметки
            notes = notes[:47] + "..."

        history_text += (
            f"{i}. {date}\n"
            f"  Продолжительность сна: {duration} часов\n"
            f"  Качество сна: {quality}/10\n"
            f"  Заметки о сне: {notes}\n\n"
        )

    bot.send_message(
        message.chat.id,
        history_text,
        reply_markup=keyboard
    )


# Обработчик команды /quality
@bot.message_handler(commands=["quality"])
def quality_info(message):
    bot.send_message(
        message.chat.id,
        "Шкала оценки качества сна:\n\n"
        "1 - Очень плохо (почти не спал)\n"
        "2-3 - Плохо\n"
        "4-5 - Средне\n"
        "6-7 - Хорошо\n"
        "8-9 - Очень хорошо\n"
        "10 - Отлично (глубокий восстанавливающий сон)",
        reply_markup=keyboard
    )


# Обработчик команды /notes
@bot.message_handler(commands=["notes"])
def notes_info(message):
    bot.send_message(
        message.chat.id,
        "Что можно записывать в заметки о сне:\n\n"
        "• Часто ли просыпался\n"
        "• Видел ли сны\n"
        "• Как себя чувствовал после пробуждения\n"
        "• Внешние факторы (шум, свет, температура)\n"
        "• Время засыпания и пробуждения\n"
        "• Общее самочувствие",
        reply_markup=keyboard
    )


if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(none_stop=True)
