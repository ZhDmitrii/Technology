"""
                                            Задание.

    Реализовать конвертер из csv в json формат: [{column -> value}, ... , {column -> value}] название столбца
— значение (аналог DictReader из модуля csv).
    Для csv формата принять разделитель между значениями, по умолчанию ","разделитель строк, по умолчанию "\n".

    В результате распечатать json строку с отступами равными 4.
"""

import csv
import json

json_array = []


def convert_csv_to_json(csv_file, json_file):
    with open(csv_file, "r", encoding="utf-8") as c_file:
        reader = csv.DictReader(c_file)

        for row in reader:
            json_array.append(row)

    with open(json_file, "w", encoding="utf-8") as j_file:
        json_string = json.dumps(json_array, ensure_ascii=False, indent=4)
        j_file.write(json_string)


def print_json_file(json_file):
    print(f"\nСодержимое файла {json_file}:")
    print("-" * 50)

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        print(json.dumps(data, ensure_ascii=False, indent=4))
        print(type("prices.json"))


csv_file = "prices.csv"
json_file = "prices.json"
convert_csv_to_json(csv_file, json_file)
print_json_file("prices.json")
