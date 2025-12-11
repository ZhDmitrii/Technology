"""
    Задание 0. Работа с json.

        ¤ Считайте данные из файла student_list.json и преобразуйте в словарь students.
"""

import json
import os
import csv


def read_student_list(file_name, print_results_1=False):
    """Считывает данные из JSON файла и преобразует в словарь students."""
    try:
        if not os.path.exists(file_name):
            print(f"Ошибка: Файл {file_name} не найден")
            return None

        with open(file_name, "r", encoding="utf-8") as f:
            students = json.load(f)

        if print_results_1:
            print(f"Данные загружены из {file_name}.")
            print(f"Загружено записей: {len(students)}.")

        return students

    except json.JSONDecodeError as e:
        print(f"Ошибка: Неверный формат в файле {file_name}.")
        print(f"Детали ошибки: {e}.")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None


def print_data():
    """Функция для демонстрации работы программы"""
    students = read_student_list(file_name="student_list.json", print_results_1=True)

    if students:
        print("=" * 50)
        print("Вывод данных:")
        print("=" * 50)

        for name, info in students.items():
            print(f"Студент: {name}")
            print(f"Возраст: {info['age']} лет")
            print(f"Предметы: {', '.join(info['subjects'])}")
            print("Оценки по предметам:")
            for subject, grade in info['grades'].items():
                print(f"  {subject}: {grade}")
            print("-" * 50)


"""
    Задание 1: Средний балл по всем предметам
        ¤ Напишите функцию get_average_score(), которая вычисляет средний балл по всем предметам для каждого студента в 
          словаре students. Выведите результат в формате:

          Средний балл для студента John: 85.0
          Средний балл для студента Alice: 83.33333333333333
          Средний балл для студента Michael: 85.0
          Средний балл для студента Sophia: 90.66666666666667
          Средний балл для студента Robert: 83.66666666666667
"""


def get_average_score(students, print_results=False):
    """Вычисляет средний балл по всем предметам для каждого студента"""
    average_scores = {}

    for name, info in students.items():
        grades = list(info["grades"].values())
        if grades:
            average_score = sum(grades) / len(grades)
        else:
            average_score = 0
        average_scores[name] = average_score

        if print_results:
            print(f"Средний балл для студента {name}: {average_score}")

    return average_scores


def print_average_score():
    """Функция для демонстрации работы программы"""
    students = read_student_list(file_name="student_list.json", print_results_1=False)

    if students:
        print("=" * 40)
        print("Средний балл студентов:")
        print("=" * 40)
        get_average_score(students, print_results=True)


"""
    Задание 2: Наилучший и худший студент
        ¤ Напишите функции get_best_student() и get_worst_student(), которые находят студента с наилучшим и худшим средним 
          баллом соответственно. Выведите их имена и средние баллы в следующем формате:

          Наилучший студент: Sophia (Средний балл: 90.67)
          Худший студент: Robert (Средний балл: 83.67)
"""


def get_best_student(students):
    """Находит студента с наилучшим средним баллом."""
    average_scores = get_average_score(students, print_results=False)
    best_student = max(average_scores.items(), key=lambda x: x[1])

    return best_student


def get_worst_student(students):
    """Находит студента с худшим средним баллом."""
    average_scores = get_average_score(students, print_results=False)
    worst_student = min(average_scores.items(), key=lambda x: x[1])

    return worst_student


def print_best_worst_student():
    """Функция для вывода лучшего и худшего студентов"""
    students = read_student_list(file_name="student_list.json", print_results_1=False)

    if students:
        print("=" * 40)
        print("Лучший и худший студенты:")
        print("=" * 40)

        best_student_name, best_score = get_best_student(students)
        worst_student_name, worst_score = get_worst_student(students)

        print(f"Наилучший студент: {best_student_name} (Средний балл: {best_score:.2f})")
        print(f"Худший студент: {worst_student_name} (Средний балл: {worst_score:.2f})")


"""
    Задание 3: Поиск по имени
        ¤ Напишите функцию find_student(name), которая принимает имя студента в качестве аргумента и выводит информацию 
          о нем, если такой студент есть в словаре students. В противном случае, выведите сообщение "Студент с таким 
          именем не найден".

          Пример:

          find_student("John")

          Вывод:

          Имя: John
          Возраст: 20
          Предметы: ['Math', 'Physics', 'History']
          Оценки: {'Math': 95, 'Physics': 88, 'History': 72}

          find_student("Emma")

          Вывод:

          Студент с таким именем не найден
"""


def find_student():
    """Поиск студента по имени и вывод информации о нём."""
    students = read_student_list(file_name="student_list.json", print_results_1=False)

    name = input("Введите имя студента: ").strip()

    found_student = None
    for student_name, student_info in students.items():
        if student_name.lower() == name.lower():
            found_student = (student_name, student_info)
            break

    if found_student:
        student_name, student_info = found_student
        print("=" * 50)
        print(f"Информация о студенте: {student_name}")
        print("=" * 50)
        print(f"Возраст: {student_info['age']} лет")
        print(f"Предметы: {', '.join(student_info['subjects'])}")
        print("Оценки по предметам:")
        for subject, grade in student_info['grades'].items():
            print(f" {subject}: {grade}")

        return found_student
    else:
        print(f"\nСтудент с именем '{name}' не найден!")
        return None


"""
   Задание 4: Сортировка студентов
        ¤ Отсортируйте студентов по их среднему баллу в порядке убывания. Выведите имена студентов и их средние баллы в 
          следующем формате:

          Сортировка студентов по среднему баллу:
          Sophia: 90.67
          Michael: 85.0
          John: 85.0
          Robert: 83.67
          Alice: 83.33          
"""


def sorted_average_scores():
    """Сортирует студентов по их среднему баллу в порядке убывания."""
    students = read_student_list(file_name="student_list.json", print_results_1=False)
    average_scores = get_average_score(students, print_results=False)

    sorted_students = sorted(average_scores.items(), key=lambda x: x[1], reverse=True)

    print("=" * 50)
    print("Сортировка студентов по среднему баллу:")
    print("=" * 50)
    for name, score in sorted_students:
        print(f"{name}: {score:.2f}")


"""
    Задание 5. Преобразуйте словарь в список словарей данного формата

            ¤ students = [
                  {
                      'name': 'John',
                      'age': 20,
                      'subjects': ['Math', 'Physics', 'History', 'Chemistry', 'English'],
                      'grades': {'Math': 95, 'Physics': 88, 'History': 72, 'Chemistry': 84, 'English': 90}
                  },
                  {
                      'name': 'Alice',
                      'age': 19,
                      'subjects': ['Biology', 'Chemistry', 'Literature', 'Math', 'Art'],
                      'grades': {'Biology': 80, 'Chemistry': 92, 'Literature': 78, 'Math': 88, 'Art': 86}
                  },
                  {
                      'name': 'Michael',
                      'age': 22,
                      'subjects': ['Computer Science', 'English', 'Art', 'History', 'Economics'],
                      'grades': {'Computer Science': 87, 'English': 78, 'Art': 90, 'History': 82, 'Economics': 75}
                  },
                  # информация о других студентах здесь
              ]
"""


def convert_dict_to_list():
    """Преобразует словарь студентов в список словарей в требуемом формате"""
    students = read_student_list(file_name="student_list.json", print_results_1=False)

    if isinstance(students, dict):
        student_list = []
        for name, info in students.items():
            student_dict = {
                "name": name,
                "age": info.get("age", 0),
                "subjects": info.get("subjects", []),
                "grades": info.get("grades", {})
            }
            student_list.append(student_dict)
        return student_list

    else:
        print(f"Неизвестный формат данных: {type(students)}")
        return []


def print_formatted_students():
    """Выводит отформатированный список студентов"""
    formatted_students = convert_dict_to_list()

    print("=" * 50)
    print("Форматированный список студентов:")
    print("=" * 50)

    for student in formatted_students:
        print(f"\nИмя: {student['name']}")
        print(f"Возраст: {student['age']}")
        print(f"Предметы: {', '.join(student['subjects'])}")
        print("Оценки:")
        for subject, grade in student['grades'].items():
            print(f" {subject}: {grade}")
        print("-" * 50)

    return formatted_students


"""
    Задание 6. Сформируйте csv
        ¤ Сформируйте файл в формате csv следующего вида

          Заголовки: name,age,grade - имя, возраст и средний балл студента 

          Данные:

          John, 20, 85.0
          Alice, 19, 83.3
          Michael, 22, 85.0
          ... 
"""


def create_student_csv():
    """Создает CSV файл с данными студентов: имя, возраст, средний балл"""
    students = read_student_list(file_name="student_list.json", print_results_1=False)
    average_scores = get_average_score(students, print_results=False)

    # Сортируем студентов по имени для удобства
    sorted_students = sorted(average_scores.items(), key=lambda x: x[0])

    # Создаем CSV файл
    with open("students.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        # Записываем заголовки
        writer.writerow(["Имя", "Возраст", "Средний балл"])

        # Записываем данные студентов
        for name, avg_score in sorted_students:
            # Получаем возраст студента
            age = students[name]["age"] if name in students else 0
            writer.writerow([name, age, f"{avg_score:.1f}"])

    print("=" * 50)
    print("CSV файл успешно создан: 'students.csv'")
    print("=" * 50)

    # Выводим содержимое файла для проверки
    print("\nСодержимое файла students.csv:")
    print("-" * 30)
    with open("students.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(', '.join(row))


if __name__ == "__main__":
    print("Задание 0: Работа с json.\n")
    print_data()
    print("Задание 1: Средний балл по всем предметам.\n")
    print_average_score()
    print("-" * 45)
    print("Задание 2: Наилучший и худший студент.\n")
    print_best_worst_student()
    print("-" * 45)
    print("Задание 3: Поиск по имени.\n")
    find_student()
    print("-" * 45)
    print("Задание 4: Сортировка студентов.\n")
    sorted_average_scores()
    print("-" * 45)
    print("Задание 5. Преобразуйте словарь в список словарей данного формата.\n")
    formatted_list = print_formatted_students()
    if formatted_list:
        with open('formatted_students.json', 'w', encoding='utf-8') as f:
            json.dump(formatted_list, f, ensure_ascii=False, indent=4)
        print("\nФорматированный список сохранен в файл 'formatted_students.json'")
    print("-" * 45)
    print("Задание 6. Сформируйте csv.\n")
    create_student_csv()
    print("-" * 45)
