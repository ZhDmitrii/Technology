"""
                                        Задание: Управление файлами и директориями.

    Часть 1: Работа с файлами и директориями.

        ¤ Создать программу, которая создаст новую директорию с именем "Управление файлами".
        ¤ В этой директории создать два файла: "file_1.txt", "file_2.txt".
        ¤ Записать в каждый из файлов какой-то текст.
        ¤ Вывести содержимое директории на экран.
"""
import os


def setup_working_directory():
    """Настройка рабочей директории."""
    current_directory = os.getcwd()
    print(f"Текущая директория: {current_directory}")
    print("-" * 65)

    # Создание и проверка на наличие новой директории
    if not os.path.isdir("Управление_файлами"):
        os.mkdir("Управление_файлами")

    # Переход в созданную директорию
    os.chdir("Управление_файлами")
    current_directory = os.getcwd()
    print(f"Текущая директория изменилась на: {current_directory}")
    print("-" * 97)

    return current_directory


def create_files():
    """Создание файлов с содержимым."""
    first_file = "file_1.txt"
    second_file = "file_2.txt"
    # Создание первого файла
    with open(first_file, "w", encoding="utf-8") as f:
        f.write("В технике всегда существовало деление на металлы и неметаллы\n")
        print(f"Создан файл: {first_file}")
        print("-" * 24)

    with open(second_file, "w", encoding="utf-8") as f:
        f.write("Причина такого деления лежит в резком\n "
                "различии свойств металлов и неметаллов - мы скоро увидим, в чем здесь дело, и\n "
                "следовательно, путей их использования.")
        print(f"Создан файл: {second_file}")
        print("-" * 24)


def list_directory_contents():
    """Вывод содержимого текущей директории."""
    files_and_dirs = os.listdir(".")
    print(f"Все файлы в текущей директории: {files_and_dirs}")
    print("-" * 91)
    return files_and_dirs


"""
    Часть 2: Удаление файлов и директории.

        ¤ Удалить один из созданных файлов.
        ¤ Создайте ещё одну поддиректорию внутри "Управление_файлами".
        ¤ Переместить оставшийся файл в эту новую поддиректорию.
        ¤ Удалить исходную директорию "Управление_файлами" вместе с её содержимым.
"""


def delete_file(file_name):
    """Удаление и проверка на наличие файла."""
    if os.path.isfile(file_name):
        os.remove(file_name)
        print(f"Удалён файл: {file_name}")
        print("-" * 24)
    else:
        print(f"Файл {file_name} не существует")
        print("-" * 24)


def create_subdirectory(dir_name):
    """Создание поддиректории."""
    os.makedirs(dir_name, exist_ok=True)
    print(f"Создана поддиректория: {dir_name}")
    print("-" * 50)


def move_file(source_file, destination_file):
    """Перемещение файла между директориями."""
    # Проверка существования исходного файла
    if os.path.exists(destination_file):
        os.remove(destination_file)
    os.rename(source_file, destination_file)
    print(f"Перемещён файл из директории: {source_file}\n"
          f"в директорию: {destination_file}")
    print("-" * 118)


def get_absolute_paths():
    """Получение абсолютных путей для операций"""
    current_dir = os.getcwd()

    paths = {
        "source_file": os.path.join(current_dir, "file_2.txt"),
        "destination_dir": os.path.join(current_dir, "Ещё_одна_управление_файлами"),
        "destination_file": os.path.join(current_dir, "Ещё_одна_управление_файлами", "file_2.txt")
    }

    return paths


def safe_remove_directory(directory_name="Управление_файлами"):
    """Безопасное удаление директории и всего её содержимого с использованием только os."""

    def remove_directory_recursive(path):
        """Рекурсивное удаление директории и её содержимого."""
        if os.path.isfile(path):
            # Если это файл - просто удаляем
            os.remove(path)
            return

        # Если это директория - рекурсивно удаляем всё содержимое
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            remove_directory_recursive(item_path)

        # После удаления всего содержимого удаляем саму директорию
        os.rmdir(path)

    # Получаем абсолютный путь к директории
    current_dir = os.getcwd()

    # Если находимся внутри удаляемой директории, выходим на уровень выше
    if os.path.basename(current_dir) == directory_name:
        os.chdir("..")
        current_dir = os.getcwd()

    target_directory = os.path.join(current_dir, directory_name)

    # Проверяем существование директории
    if not os.path.exists(target_directory):
        print(f"Директория '{directory_name}' не существует.")
        print("-" * 50)
        return False

    # Проверяем, что это действительно директория
    if not os.path.isdir(target_directory):
        print(f"'{directory_name}' не является директорией.")
        print("-" * 50)
        return False

    # Запрашиваем подтверждение у пользователя
    print(f"Внимание: вы собираетесь удалить директорию '{directory_name}' и ВСЁ её содержимое!")
    print("Это действие невозможно отменить.")
    confirmation = input("Вы уверены? (да/нет):").lower().strip()

    if confirmation in ["да", "д", "yes", "y"]:
        try:
            # Удаляем директорию рекурсивно
            remove_directory_recursive(target_directory)
            print(f"Директория '{directory_name}' и всё её содержимое успешно удалены.")
            print("-" * 70)
            return True
        except PermissionError as e:
            print(f"Ошибка доступа: {e}")
            print("Возможно некоторые файлы заняты другими процессами.")
            print("-" * 50)
            return False
        except Exception as e:
            print(f"Ошибка при удалении директории: {e}")
            print("-" * 50)
            return False
    else:
        print("Удаление отменено.")
        print("-" * 24)
        return False


def main():
    """Основная функция, выполняющая все операции"""
    print("ЗАПУСК ПРОГРАММЫ УПРАВЛЕНИЯ ФАЙЛАМИ")
    print("=" * 35)

    # 1. Настройка рабочей директории
    setup_working_directory()

    # 2. Создание файлов
    create_files()

    # 3. Показать содержимое директории
    list_directory_contents()

    # 4. Удаление файла
    delete_file("file_1.txt")

    # 5. Создание поддиректории
    create_subdirectory("Ещё_одна_управление_файлами")

    # 6. Перемещение файла
    paths = get_absolute_paths()
    move_file(paths["source_file"], paths["destination_file"])

    # 7. Безопасное удаление всей директории
    safe_remove_directory("Управление_файлами")


# Запуск программы
if __name__ == "__main__":
    # Используйте main() для автоматического определения путей
    main()
