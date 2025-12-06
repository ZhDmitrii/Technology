"""
                                                 Задание.

    1. Используйте map(), чтобы преобразовать список чисел в список их кубов, используя обычную функцию.
"""


def cube(x):
    """Возвращает куб числа x."""
    return x ** 3


def convert_to_cubes(function, iterable):
    """Преобразует список чисел в список их кубов с помощью map()."""
    return list(map(function, iterable))


"""
    2. Используйте filter(), чтобы отобрать из списка чисел только те, которые делятся на 5, используя обычную функцию. 
"""


def is_divisible_by_5(x):
    """Проверяет, делится ли число x на 5 без остатка."""
    return x % 5 == 0


def filter_divisible_by_5(function, iterable):
    """Отбирает из списка чисел только те, которые делятся на 5, используя filter()."""
    return list(filter(function, iterable))


"""
    3. Используйте  filter() и  reduce(), чтобы найти произведение всех нечетных чисел в списке, используя обычную функцию.
"""

from functools import reduce


def is_uneven(x):
    """Проверяет, является ли число x нечетным."""
    return x % 2 != 0


def multiply(x, y):
    """Возвращает произведение чисел в списке."""
    return x * y


def mult_of_uneven_numbers(function, iterable):
    """Находит произведение всех нечетных чисел в списке, используя filter() и reduce()."""
    # Отбираем нечетные числа с помощью filter()
    uneven_numbers = list(filter(is_uneven, numbers_1))

    # Вычисляем произведение нечетных чисел с помощью reduce()
    mult = reduce(multiply, uneven_numbers)
    return mult


if __name__ == "__main__":
    print("Задание №1:")
    numbers = [1, 2, 3, 4, 5]
    cubes = convert_to_cubes(cube, numbers)
    print("Кубы чисел:", cubes)
    print("-" * 45)

    print("Задание №2:")
    numbers_0 = [10, 12, 15, 20, 22, 25, 30]
    divisible_by_5 = filter_divisible_by_5(is_divisible_by_5, numbers_0)
    print("Числа, делящиеся на 5:", divisible_by_5)
    print("-" * 45)

    print("Задание №3:")
    numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = mult_of_uneven_numbers(multiply, numbers_1)
    print("Произведение нечетных чисел:", result)
    print("-" * 45)
