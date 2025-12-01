"""
                                                   Задание.

    Задача 1: Комбинация чисел из списка.

        ¤ Дан список чисел [1, 2, 3, 4]. Используя модуль itertools, создайте все возможные комбинации чисел длиной два
          и выведите их.
"""

import itertools


def generate_combinations(iterable, r):
    """Генерирует все комбинации заданной длины из списка."""
    return list(itertools.combinations(iterable, r))


def generate_combinations_with_replacement(iterable, r):
    """Генерирует все комбинации заданной длины из списка."""
    return list(itertools.combinations_with_replacement(iterable, r))


def generate_permutations(iterable, r=None):
    """Генерирует все комбинации заданной длины из списка."""
    return list(itertools.permutations(iterable, r))


"""
    Задача 2: Перебор перестановок букв в слове.

        ¤ Для слова 'Python' найдите все возможные перестановки букв.
          Выведите каждую перестановку на отдельной строке.
"""


def generate_word_permutations(iterable):
    """Генерирует все возможные перестановки букв в слове."""

    result = list(itertools.permutations(iterable))

    return result


def print_permutations(result):
    """Выводит все перестановки на отдельных строках."""

    for perm in result:
        print(perm)


"""
    Задача 3: Объединение списков в цикле.

        ¤ Даны три списка: ['a', 'b'], [1, 2, 3], ['x', 'y']. Используя itertools.cycle, объедините их в один список
          в цикле,повторяя этот цикл 5 раз.
"""


def combine_lists_with_cycle(list_1, list_2, list_3, cycles=5):
    """Объединяет три списка в один, циклически повторяя элементы."""

    # Создаём бесконечные циклы для каждого списка
    cycle_1 = itertools.cycle(list_1)
    cycle_2 = itertools.cycle(list_2)
    cycle_3 = itertools.cycle(list_3)

    result = []

    # Выполняем заданное количество циклов
    for _ in range(cycles):
        # Берём по одному элементу из каждого цикла
        result.append(next(cycle_1))
        result.append(next(cycle_2))
        result.append(next(cycle_3))

    return result


""" 
    Задача 4: Генерация бесконечной последовательности чисел.

        ¤ Создайте бесконечный генератор, который будет возвращать последовательность чисел Фибоначчи.
          Выведите первые 10 чисел Фибоначчи.
"""


def fibonacci_generator():
    """Бесконечный генератор чисел Фибоначчи."""

    class FibonacciIterator:
        def __init__(self):
            self.a, self.b = 0, 1

        def __iter__(self):
            return self

        def __next__(self):
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            return result

    return FibonacciIterator()


def get_first_n_fibonacci(n):
    """Возвращает первые n чисел Фибоначчи"""
    fib_gen = fibonacci_generator()
    return list(itertools.islice(fib_gen, n))


"""
    Задача 5: Составление всех возможных комбинаций слов.

        ¤ Используя itertools.product, создайте все возможные комбинации слов из двух списков:
          ['red', 'blue'] и ['shirt', 'shoes']. Выведите каждую комбинацию на отдельной строке.
"""

import itertools


def generate_combination(*iterables):
    """Генерирует все возможные комбинации слов из двух списков."""
    colors = ['red', 'blue']
    items = ['shirt', 'shoes']

    combination = itertools.product(colors, items)

    for color, item in combination:
        print(f"{color} {item}")


if __name__ == "__main__":
    num = [1, 2, 3, 4]

    print("Задача 1: Комбинация чисел из списка.\n")

    result1 = generate_combinations(num, 2)
    print("Комбинации (combinations):")
    print(result1)
    print()

    result2 = generate_combinations_with_replacement(num, 2)
    print("Комбинации с повторениями (combinations_with_replacement):")
    print(result2)
    print()

    result3 = generate_permutations(num, 2)
    print("Перестановки (permutations):")
    print(result3)
    print("-" * 100)

    print("Задача 2: Перебор перестановок букв в слове.\n")

    word = "Python"

    print(f"Все перестановки для слова '{word}':\n")
    permutations = generate_word_permutations(word)
    print_permutations(permutations)
    print(f"\nВсего перестановок: {len(permutations)}")
    print("-" * 30)

    print("Задача 3: Объединение списков в цикле.\n")

    list_a = ["a", "b"]
    list_b = [1, 2, 3]
    list_c = ["x", "y"]

    print("Исходные списки:")
    print(f"list1: {list_a}")
    print(f"list2: {list_b}")
    print(f"list3: {list_c}\n")

    print("Результат:")
    result4 = combine_lists_with_cycle(list_a, list_b, list_c, cycles=5)
    print(result4)
    print("-" * 66)

    print("Задача 4: Генерация бесконечной последовательности чисел.\n")

    first_10_fibonacci = get_first_n_fibonacci(10)
    print(f"Первые 10 чисел Фибоначчи: {first_10_fibonacci}")
    print("-" * 66)

    print("Задача 5: Составление всех возможных комбинаций слов.\n")
    print("Возможные комбинации слов:")
    generate_combination()
    print("-" * 30)
