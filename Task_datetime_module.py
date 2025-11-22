"""
                                          Операции с датой и временем.

    Часть 1. Работа с текущей датой и временем:

        ¤ Получить текущую дату и время.
        ¤ Вывести на экран день недели для этой даты.
        ¤ Определить, является ли год текущей даты високосным, и вывести соответствующее сообщение.
"""

import datetime


def get_current_datetime_and_details():
    """Функция возвращает текущую дату и время, определяет день недели и проверяет, является ли год високосным"""
    # Получаем текущую дату и время
    current_date_and_time = datetime.datetime.now()

    # Определяем день недели
    week_day = current_date_and_time.strftime("%A")

    # Определяем, является ли год високосным
    which_year = current_date_and_time.year % 4 == 0 and current_date_and_time.year % 100 != 0 or current_date_and_time.year % 400 == 0
    if which_year:
        message = "год високосный."
    else:
        message = "год не високосный."

    result = (f"Текущая дата и время: {current_date_and_time.strftime("%d-%m-%Y %H:%M:%S")}.\n"
              f"День недели: {week_day}.\n"
              f"Информация о годе: {current_date_and_time.year} {message}.")
    return result


if __name__ == '__main__':
    details = get_current_datetime_and_details()
    print(details)
    print("-" * 42)

"""
    Часть 2. Работа с пользовательской датой:

        ¤ Запросить у пользователя ввод даты в формате "год-месяц-день" (например, "2023-12-31")
        ¤ Определить, сколько дней осталось до введённой даты от текущей даты.
        ¤ Рассчитать разницу между этими двумя датами и вывести результат в формате дней, часов, минут. 
"""


def find_how_many_days(input_date_str):
    """Функция вычисляет сколько дней до введённой пользователем даты."""
    # Получаем текущую дату и время
    cur_date_and_time = datetime.datetime.now()

    try:
        # Преобразуем строку ввода в объект datetime
        received_date = datetime.datetime.strptime(input_date_str, "%Y-%m-%d")

        # Вычисляем разницу между введённой датой и текущей датой
        delta = received_date - cur_date_and_time

        if delta.days >= 0:
            # Разбиваем разницу на дни, часы и минуты
            total_seconds = int(delta.total_seconds())
            days = delta.days
            hours, remainder = divmod(total_seconds % 86400, 3600)
            minutes, _ = divmod(remainder, 60)

            return f"Дней осталось: {days}, Часов: {hours}, Минут: {minutes}."
        else:
            return "Указанная дата уже прошла."
    except ValueError:
        return "Ошибка формата даты. Убедитесь, что ввели дату в формате 'год-месяц-день'."


if __name__ == "__main__":
    input_date = input("Введите дату в формате 'год-месяц-день': ")
    res = find_how_many_days(input_date)
    print(res)
    print("-" * 42)
