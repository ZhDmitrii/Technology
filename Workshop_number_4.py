"""
                                                Практикум 4.

    Задача 1:
        ¤ Дан словарь учеников. Отсортировать учеников по возрасту.
"""


def sort_students_by_age(students_dict):
    """Сортирует словарь учеников по возрасту."""
    sorted_students = sorted(students_dict.items(), key=lambda item: item[1])
    return sorted_students


def main():
    students_dict = {
        "Саша": 27,
        "Кирилл": 52,
        "Маша": 14,
        "Петя": 36,
        "Оля": 43,
    }

    print("Исходный словарь студентов:")
    print("-" * 20)
    print("  Имя  | Возраст")
    print("-" * 20)
    for name, age in students_dict.items():
        print(f"{name:^6} | {age} лет")

    print("\nСортировка по возрасту (возрастание):")
    print("-" * 20)
    print("  Имя  | Возраст")
    print("-" * 20)
    sorted_students = sort_students_by_age(students_dict)
    for name, age in sorted_students:
        print(f"{name:^6} | {age} лет.")

    print("\nСортировка по возрасту (убывание):")
    print("-" * 20)
    print("  Имя  | Возраст")
    print("-" * 20)
    sorted_dict = sorted(students_dict.items(), key=lambda item: item[1], reverse=True)
    for name, age in sorted_dict:
        print(f"{name:^6} | {age} лет.")


"""
    Задача 2:
        ¤ Дан список с данными о росте и весе людей. Отсортировать их по индексу массы тела. Он вычисляется по формуле: 
          Вес тела в килограммах/(Рост в метрах∗Рост в метрах).
"""


def calculate_bmi(weight_kg, height_cm):
    """Вычисляет индекс массы тела (ИМТ)."""
    height_m = height_cm / 100
    bmi = weight_kg / (height_m * height_m)
    return round(bmi, 2)


def sort_by_bmi(data):
    """Сортирует список по ИМТ."""
    # Создаём список с добавлением ИМТ.
    data_with_bmi = [(weight, height, calculate_bmi(weight, height))
                     for weight, height in data]
    # Сортируем по ИМТ с помощью лямбда-функции
    sorted_data = sorted(data_with_bmi, key=lambda x: x[2])

    return sorted_data


def print_result(data):
    """Выводит результаты в удобном формате."""

    print("Вес (кг) | Рост (см) | ИМТ    | Категория")
    print("-" * 50)

    for weight, height, bmi in data:
        # Определяем категорию по ИМТ
        if bmi < 18.5:
            category = "Недостаточный вес"
        elif bmi < 25:
            category = "Нормальный вес"
        elif bmi < 30:
            category = "Избыточный вес"
        else:
            category = "Ожирение"

        print(f"{weight:^8} | {height:^9} | {bmi:^6.2f} | {category}")


def main_1():
    data = [
        (82, 191),
        (68, 174),
        (90, 189),
        (73, 179),
        (76, 184)
    ]

    print("Исходные данные:")
    print("-" * 20)
    print("Вес (кг) | Рост (см)")
    print("-" * 20)
    for weight, height in data:
        print(f"{weight:^8} | {height:^8}")

    print("\n" + "=" * 50)
    print("Сортировка по ИМТ:")
    print("=" * 50)

    sorted_data = sort_by_bmi(data)

    print_result(sorted_data)

    print("\n" + "=" * 50)
    print("Сортировка по ИМТ (убывание):")
    print("=" * 50)

    sorted_data_1 = sorted(sort_by_bmi(data), key=lambda x: x[2], reverse=True)
    print_result(sorted_data_1)


"""
    Задача 3:
        ¤ Дан словарь учеников. Найти самого минимального ученика по возрасту.
"""


def find_youngest_student_name(students_list):
    """Находит самого младшего ученика в списке."""
    youngest = min(students_list, key=lambda student: student["age"])
    return youngest


def main_2():
    students_list = [
        {
            "name": "Саша",
            "age": 27,
        },
        {
            "name": "Кирилл",
            "age": 52,
        },
        {
            "name": "Маша",
            "age": 14,
        },
        {
            "name": "Петя",
            "age": 36,
        },
        {
            "name": "Оля",
            "age": 43,
        },
    ]

    youngest = find_youngest_student_name(students_list)

    print("Исходный словарь учеников:")
    print("-" * 20)
    print("  Имя  | Возраст")
    print("-" * 20)
    for student in students_list:
        print(f"{student["name"]:^6} | {student["age"]} лет")

    print(f"\nСамый младший ученик: {youngest['name']}, возраст: {youngest['age']}")


if __name__ == "__main__":
    print("Задача №1:\n")
    main()
    print("-" * 45)
    print("Задача №2:\n")
    main_1()
    print("-" * 50)
    print("Задача №3:\n")
    main_2()
    print("-" * 45)
