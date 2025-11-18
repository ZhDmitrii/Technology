"""
                                Задание 1: Работа с JSON файлом.

                                Задача:

    Предлагается JSON файл с данными о студентах. Необходимо создать программу, которая проведёт анализ этих
данных и выведет информацию на экран.
        1. Прочитать данные из файла student.json.
        2. Определить общее количество студентов в файле.
        3. Найти самого взрослого студента и вывести его данные (имя, возраст, город).
        4. Определить количество студентов, изучающих предмет.

"""

import json


def create_json_file(file_name):
    """Функция для записи в JSON файл"""

    students = [
        {
            "имя": "Анна",
            "возраст": 20,
            "город": "Москва",
            "предметы": ["Python", "JavaScript"]
        },
        {
            "имя": "Пётр",
            "возраст": 22,
            "город": "Санкт-Петербург",
            "предметы": ["Python", "Java"]
        },
        {
            "имя": "Мария",
            "возраст": 21,
            "город": "Киев",
            "предметы": ["JavaScript", "SQL"]
        }
    ]

    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=4)

    print("\nЗадание №1. Работа с JSON файлом:")
    print(f"Файл {file_name} успешно создан.")
    print("-" * 30)


def read_json_file(file_name):
    """Функция для чтения данных из JSON файла"""
    with open(file_name, "r", encoding="utf-8") as f:
        return json.load(f)


def total_number_of_students(students):
    """Функция для подсчёта общего количества студентов"""
    return len(students)


def find_the_most_adult_student(students):
    """Функция для поиска самого взрослого студента"""
    adult = max(students, key=lambda x: x["возраст"])
    return adult


def count_students_by_subject(students, subject):
    """Определяет количество студентов, изучающих определенный предмет"""
    count = 0
    for student in students:
        if subject in student["предметы"]:
            count += 1
    return count


file_name = "students.json"

create_json_file(file_name)

students = read_json_file(file_name)
print(f"Перечень студентов:{students}")
print("-" * 30)

num_students = total_number_of_students(students)
print(f"Общее количество студентов: {num_students}")
print("-" * 30)

adult_student = find_the_most_adult_student(students)
print(f"Самый старший студент: \nИмя: {adult_student["имя"]}, \nВозраст: {adult_student["возраст"]},"
      f"\nГород: {adult_student["город"]}")
print("-" * 30)

print("Количество студентов по предмету.")
subjects = ["Python", "JavaScript", "SQL"]
for subject in subjects:
    count = count_students_by_subject(students, subject)
    print(f"Изучающие {subject}: {count} студент(ов).")
print("-" * 30)

"""        
                                Задание 2: Работа с CSV файлом.

                                Задача:

    Предлагается файл в формате CSV с данными о продажах в компании. Задача обработать этот файл и получить
полезную информацию.
        1. Считать данные из файла sales.csv.
        2. Подсчитать общую сумму продаж за весь период.
        3. Определить продукт с самым высоким объёмом продаж и вывести его на экран.
        4. Разделить данные на категории по месяцам и вывести общую сумму продаж для каждого месяца.

"""

import csv


def convert_txt_to_csv(txt_file, csv_file):
    """Функция преобразует текстовый файл (*.txt) в CSV-файл (*.csv)."""
    with open(txt_file, "r", encoding="utf-8") as t_file:
        lines = t_file.readlines()
        fieldnames = [column.strip() for column in lines.pop(0).strip().split(",")]  # Удаляем лишние пробелы
        data = []
        for line in lines:
            row = line.strip().split(",")
            entry = {}
            for idx, part in enumerate(row):
                entry[fieldnames[idx]] = part.strip()  # Убираем лишние пробелы и из данных тоже
            data.append(entry)

        with open(csv_file, "w", newline="", encoding="utf-8") as c_file:
            writer = csv.DictWriter(c_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        print("\nЗадание №2. Работа с CSV файлом:\nПреобразование успешно выполнено.")
        print("-" * 50)


def print_csv_file(csv_file):
    """Функция считывает и выводит на экран содержимое CSV файла."""
    print(f"Содержимое файла {csv_file}:")

    with open(csv_file, "r", encoding="utf-8") as c_file:
        reader = csv.reader(c_file)
        for i, row in enumerate(reader):
            print(f"Строка {i}: {row}")


def calculate_total_sales(data):
    """Функция подсчитывает общую сумму продаж за весь период."""
    total_sum = sum(int(row["Сумма"]) for row in data)
    return total_sum


def find_best_selling_product(data):
    """Функция находит продукт с самым большим объёмом продаж."""
    product_sales = {}

    for row in data:
        product_name = row["Продукт"]
        amount = int(row["Сумма"])

        if product_name in product_sales:
            product_sales[product_name] += amount
        else:
            product_sales[product_name] = amount

    best_seller = max(product_sales.items(), key=lambda x: x[1])

    return best_seller


def find_amount_of_sales_for_each_month(csv_file):
    """Функция возвращает общий объём продаж по месяцам."""
    sales_by_month = {}

    with open(csv_file, "r", encoding="utf-8") as c_file:
        reader = csv.DictReader(c_file)

        for row in reader:
            date_parts = row["Дата"].split("-")
            month = int(date_parts[1])
            amount = int(row["Сумма"])
            if month not in sales_by_month:
                sales_by_month[month] = 0.0
            sales_by_month[month] += amount

    return sales_by_month


with open("sales.csv", "r", encoding="utf-8") as c_file:
    reader = csv.DictReader(c_file)
    data = list(reader)

csv_file = "sales.csv"
txt_file = "sales.txt"

convert_txt_to_csv(txt_file, csv_file)
print_csv_file(csv_file)

print("-" * 50)
total_sales_amount = calculate_total_sales(data)
print(f"Общая сумма продаж за весь период: {total_sales_amount} рублей.")

print("-" * 50)
best_product, total_sales = find_best_selling_product(data)
print(f"Продукт с самым высоким объёмом продаж: {best_product}\nОбщая сумма продаж: {total_sales}.")

print("-" * 50)
result = find_amount_of_sales_for_each_month(csv_file)
for month, total_sales in sorted(result.items()):
    print(f"Месяц {month}: Общая сумма продаж — {total_sales} рублей.")
print("-" * 50)

"""

                                Задание 3: Комбинированная работа с JSON и CSV файлами.

                                Задача:

    Предоставляется два файла — JSON с информацией о сотрудниках и CSV с данными об их производительности.
Задача: Соединить эти данные для анализа.
        1. Считать данные из файлов employees.json и performance.csv.
        2. Сопоставить данные о производительности каждого сотрудника с их соответствующей из JSON файла.
        3. Определить среднюю производительность среди всех сотрудников и вывести её.
        4. Найти сотрудника с наивысшей производительностью и вывести его имя и показатель производительности.

"""


def create_j_file(j_file):
    """Функция для записи в JSON файл"""

    employees = [
        {
            "id": 1,
            "имя": "Иван",
            "должность": "Менеджер"
        },
        {
            "id": 2,
            "имя": "Елена",
            "должность": "Аналитик"
        },
        {
            "id": 3,
            "имя": "Дмитрий",
            "должность": "Разработчик"
        }
    ]

    with open(j_file, "w", encoding="utf-8") as f:
        json.dump(employees, f, ensure_ascii=False, indent=4)

    print("\nЗадание №3. Комбинированная работа с JSON и CSV файлами:")
    print(f"Файл {j_file} успешно создан.")
    print("-" * 50)


def convert_txt_to_csv(tx_file, cs_file):
    """Функция преобразует текстовый файл (*.txt) в CSV-файл (*.csv)."""
    with open(tx_file, "r", encoding="utf-8") as t_file:
        lines = t_file.readlines()
        fieldnames = [column.strip() for column in lines.pop(0).strip().split(",")]  # Удаляем лишние пробелы
        data = []
        for line in lines:
            row = line.strip().split(",")
            entry = {}
            for idx, part in enumerate(row):
                entry[fieldnames[idx]] = part.strip()  # Убираем лишние пробелы и из данных тоже
            data.append(entry)

        with open(cs_file, "w", newline="", encoding="utf-8") as c_file:
            writer = csv.DictWriter(c_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        print("Преобразование из txt файла csv файл успешно выполнено.")
        print("-" * 50)


def print_csv_file(cs_file):
    """Функция считывает и выводит на экран содержимое CSV файла."""
    print(f"Содержимое файла {cs_file}:")

    with open(cs_file, "r", encoding="utf-8") as c_file:
        reader = csv.reader(c_file)
        for i, row in enumerate(reader):
            print(f"Строка {i}: {row}")


def reads_employees_from_json(j_file):
    """Функция читает данные о сотрудниках из JSON."""
    with open(j_file, "r", encoding="utf-8") as j_file:
        return json.load(j_file)


def reads_performance_from_csv(cs_file):
    """Функция читает данные о сотрудниках из CSV файла."""
    with open(cs_file, "r", encoding="utf-8") as cs_file:
        reader = csv.reader(cs_file)
        next(reader)
        return [(row[0], float(row[1])) for row in reader]


def calculate_statistics(employees, performances):
    """Функция рассчитывает среднюю производительность и находит сотрудника с наивысшей производительностью."""
    # Совмещение данных
    combined_data = {}
    for employee in employees:
        combined_data[int(employee["id"])] = {"имя": employee["имя"],
                                              "должность": employee["должность"],
                                              "производительность": None}

    for employee_id, performance_value in performances:
        if int(employee_id) in combined_data:
            combined_data[int(employee_id)]["производительность"] = performance_value

    # Подсчёт средней производительности
    total_performance = sum(info["производительность"] for info in combined_data.values())
    average_performance = total_performance / len(combined_data)

    # Нахождение сотрудника с наивысшей производительностью
    best_employee = max(combined_data.items(), key=lambda item: item[1]["производительность"])

    return average_performance, best_employee


j_file = "employees.json"
create_j_file(j_file)

tx_file = "performance.txt"
cs_file = "performance.csv"

convert_txt_to_csv(tx_file, cs_file)
print_csv_file(cs_file)

employees = reads_employees_from_json(j_file)
performances = reads_performance_from_csv(cs_file)

avg_perf, top_emp = calculate_statistics(employees, performances)

print("-" * 50)
print(f"Средняя производительность сотрудников: {avg_perf} kpi.")
print("-" * 50)
print(f"Сотрудник с наивысшей производительностью: {top_emp[1]["имя"]},"
      f" Производительность: {top_emp[1]["производительность"]} kpi.")
