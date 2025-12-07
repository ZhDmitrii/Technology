"""
                                               Задание.

    1. Дан список строк ["apple", "kiwi", "banana", "fig"]. Оставьте в нем только строки, длина которых больше 4 символов,
       используя filter() и лямбда-функцию.
"""

strings = ["apple", "kiwi", "banana", "fig"]
strings_four = list(filter(lambda x: len(x) > 4, strings))
print("Задание №1:")
print(strings_four)  # Вывод: ['apple', 'banana']
print("-" * 45)

"""
    2. Дан список словарей students = [{"name": "John", "grade": 90}, {"name": "Jane", "grade": 85}, 
       {"name": "Dave", "grade": 92}]. Найдите студента с максимальной оценкой, используя max() и лямбда-функцию для 
       задания ключа сортировки.
"""

students = [
    {"name": "John", "grade": 90},
    {"name": "Jane", "grade": 85},
    {"name": "Dave", "grade": 92}
]
student_max = max(students, key=lambda student: student["grade"])
print("Задание №2:")
print(student_max)  # Вывод: {'name': 'Dave', 'grade': 92}
print("-" * 45)

"""
   3. Дан список кортежей [(1, 5), (3, 2), (2, 8), (4, 3)]. Отсортируйте его по сумме элементов каждого кортежа с 
      использованием sorted() и лямбда-функции. 
"""

list_tuples = [(1, 5), (3, 2), (2, 8), (4, 3)]
sum_tuples = sorted(list_tuples, key=lambda item: item[0] + item[1])
print("Задание №3:")
print(sum_tuples)  # Вывод: [(3, 2), (1, 5), (4, 3), (2, 8)]
print("-" * 45)

"""
    4. Дан список чисел [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Оставьте в нем только четные числа с использованием filter() и 
       лямбда-функции.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Задание №4:")
print(even_numbers)  # Вывод: [2, 4, 6, 8, 10]
print("-" * 45)

"""
   5. Сортировка объектов пользовательского класса:
        ¤ Создайте класс Person с атрибутами name и age. Дан список объектов этого класса. Отсортируйте список объектов 
          по возрасту с использованием sorted() и лямбда-функции. 
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"


people = [
    Person("Анна", 25),
    Person("Иван", 30),
    Person("Мария", 22),
    Person("Петр", 28)
]

sorted_persons = sorted(people, key=lambda person: person.age, reverse=True)
print("Задание №5:")
print(sorted_persons)
print("-" * 120)
"""Вывод: 
[
Person(name='Иван', age=30),
Person(name='Петр', age=28),
Person(name='Анна', age=25),
Person(name='Мария', age=22) 
]"""
