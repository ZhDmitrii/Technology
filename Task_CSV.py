"""
                                        Задание №1.

    Имеется текстовый файл prices.txt с информацией о заказе из интернет-магазина. В нем каждая строка с
помощью символа табуляции \t разделена на три колонки: наименование товара; количество товара (целое число);
цена (в рублях) товара за 1 шт. (целое число). Напишите программу, преобразующую данные из txt в csv.

"""

import csv


def convert_txt_to_csv(txt_file, csv_file, delimiter="\t"):
    with open(txt_file, "r", newline="", encoding="utf-8") as t_file:
        with open(csv_file, "w", newline="", encoding="utf-8") as c_file:
            csv_writer = csv.writer(c_file)
            lines = t_file.readlines()

            header = lines[0].strip().split(delimiter)
            csv_writer.writerow(header)

            for line in lines[1:]:
                row = line.strip().split(delimiter)
                csv_writer.writerow(row)


def print_csv_file(csv_file):
    print(f"\nСодержимое файла {csv_file}:")
    print("-" * 50)

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            print(f"Строка {i}: {row}")


# Использование
convert_txt_to_csv("prices.txt", "prices.csv", delimiter='\t')
print_csv_file("prices.csv")

"""
                                       Задание №2.

    Имеется файл prices.csv (сформированный в прошлом задании) с информацией о заказе из интернет-магазина. 
В нем каждая строка содержит три колонки: наименование товара; количество товара (целое число); 
цена (в рублях) товара за 1 шт. (целое число). Напишите программу, подсчитывающую общую стоимость заказа.

"""


def calculate_price(csv_file):
    total = 0
    with open(csv_file, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            if len(row) >= 3:
                quantity = int(row[1])
                price = int(row[2])
                total += price * quantity

    return total


total_cost = calculate_price("prices.csv")
print("-" * 50)
print(f"Общая стоимость заказа: {total_cost} рублей.")
