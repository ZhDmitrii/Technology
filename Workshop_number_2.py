"""
                                                Практикум №2.

    Задание 1: Анализ списка чисел с помощью Counter.

        ¤ 1. Сгенерировать случайный список чисел.
        ¤ 2. Использовать Counter, чтобы подсчитать количество уникальных элементов в списке.
        ¤ 3. Найти три наиболее часто встречающихся элемента в списке и вывести их с количеством вхождений.
"""

import random
from collections import Counter


def analyze_random_number():
    """Функция возвращает три наиболее часто встречающихся элемента."""
    # Генерация случайного списка из 20 чисел в диапазоне от 1 до 10
    random_numbers = [random.randint(1, 10) for _ in range(20)]

    # Используем Counter для подсчёта уникальных элементов
    count_unique = Counter(random_numbers)

    # Получаем три наиболее часто встречающихся элемента
    three_most_common = count_unique.most_common(3)

    print("-" * 90)
    print("Задание 1: Анализ списка чисел с помощью Counter.\n")
    print(f"Случайный список чисел: {random_numbers}")
    print("Подсчёт уникальных элементов:", dict(count_unique))
    print("Три наиболее часто встречающихся элемента в списке: ")
    for num, freq in three_most_common:
        print(f"{num}: {freq}")
    print("-" * 90)


if __name__ == "__main__":
    analyze_random_number()

"""
    Задание 2: Работа с именованными кортежами.

        ¤ 1. Создать именованный кортеж Book с полями title, author, genre.
        ¤ 2. Создать несколько экземпляров Book.
        ¤ 3. Вывести информацию о книгах, используя атрибуты именованных кортежей.
"""

from collections import namedtuple


def create_namedtuple():
    # Создание именованного кортежа Book
    Book = namedtuple("Book", ["title", "author", "genre"])

    # Создание экземпляров
    book_1 = Book(title="Мастер и Маргарита", author="Михаил Булгаков", genre="Роман-фэнтези")
    book_2 = Book(title="Анна Каренина", author="Лев Толстой", genre="Роман")

    print("Задание 2: Работа с именованными кортежами.\n")
    # Вывод информации о книгах
    for book in [book_1, book_2]:
        print(f"Книга: {book.title}, Автор: {book.author}, Жанр: {book.genre}")
    print("-" * 90)


if __name__ == "__main__":
    create_namedtuple()

"""
    Задание 3: Работа с defaultdict.

        ¤ 1. Создать defaultdict с типом данных list.
        ¤ 2. Добавить несколько элементов в словарь, используя ключи и значения.
        ¤ 3. Вывести содержимое словаря, где значения - это списки элементов с одинаковыми ключами.
"""

from collections import defaultdict


def demonstrate_defaultdict():
    """Функция демонстрирует работу с defaultdict с типом данных list"""
    # Создание defaultdict с типом данных list
    my_dict = defaultdict(list)

    # Добавление элементов в словарь
    my_dict["fruits"].append("apple")
    my_dict["fruits"].append("banana")
    my_dict["fruits"].append("orange")

    my_dict["vegetables"].append("carrot")
    my_dict["vegetables"].append("broccoli")

    my_dict["colors"].append("red")
    my_dict["colors"].append("blue")
    my_dict["colors"].append("green")

    print("Задание 3: Работа с defaultdict.\n")
    # Выведение содержимого словаря
    print("Содержимое defaultdict:")
    for key, value in my_dict.items():
        print(f"Ключ '{key}': {value}")

    return my_dict


if __name__ == "__main__":
    result_dict = demonstrate_defaultdict()

    # Проверка работы defaultdict
    print("\nПроверка работы с несуществующим ключом:")
    print(f"my_dict['new_key']: {result_dict["new_key"]}")
    print(f"Словарь после обращения к несуществующему ключу: {dict(result_dict)}")
    print("-" * 180)

"""
    Задание 4: Использование deque для обработки данных.

        ¤ 1. Создать deque и добавить в него элементы.
        ¤ 2. Использовать методы append, appendleft, pop, popleft для добавления и удаления элементов из deque.
        ¤ 3. Проверить, как изменится deque после каждой операции.
"""

from collections import deque


def demonstrate_deque():
    """Демонстрирует работу двусторонней очереди из модуля collections."""
    # Создаём пустую двустороннюю очередь
    my_deque = deque()
    print("Задание 4: Использование deque для обработки данных.\n")
    print(f"Создана пустой двусвязный список(deque): {my_deque}.\n")

    # Добавляем элементы в конец
    my_deque.append("первый")
    my_deque.append("второй")
    my_deque.append("третий")
    print(f"Deque после добавления элементов в конец: {my_deque}.\n")

    # Добавляем элементы в начало
    my_deque.appendleft("ноль")
    my_deque.appendleft("минус один")
    print(f"Deque после добавления элементов в начало: {my_deque}.\n")

    # Удаляем элемент с конца
    removed_end = my_deque.pop()
    print(f"Удалён элемент с конца: {removed_end}.")
    print(f"Deque после удаления с конца: {my_deque}.\n")

    # Удаляем элемент с начала
    removed_start = my_deque.popleft()
    print(f"Удалён элемент сначала: {removed_start}.")
    print(f"Deque после удаления с начала: {my_deque}.\n")

    # Продемонстрируем ещё несколько операций
    print("Дополнительные операции:")
    print(f"Текущий размер deque: {len(my_deque)}.")
    print(f"Первый элемент: {my_deque[0]}.")
    print(f"Последний элемент: {my_deque[-1]}.\n")

    return my_deque


if __name__ == "__main__":
    result_deque = demonstrate_deque()

    # Дополнительные данные
    print(f"Финальное состояние deque: {result_deque}.")
    print(f"Тип объекта: {type(result_deque)}.")
    print("-" * 90)
    print("Задание 5: Реализация простой очереди с помощью deque.\n")
"""
    Задание 5: Реализация простой очереди с помощью deque.

        ¤ 1. Написать функцию для добавления и извлечения элементов из deque.
        ¤ 2. Создать пустой deque.
        ¤ 3. Использовать написанную функцию для добавления и извлечения элементов из очереди.
"""

from collections import deque


def create_deque():
    """Создаёт и возвращает пустую очередь."""
    return deque()


def enqueue(queue, item):
    """Добавляет элемент в конец очереди."""
    queue.append(item)
    print(f"Добавлен элемент в конец очереди: '{item}'.")


def dequeue(queue):
    """Извлекает и возвращает элемент из начала очереди. Возвращает None, если очередь пуста."""
    if not queue:
        print("Очередь пуста, невозможно извлечь элемент.")
        return None
    item = queue.popleft()
    print(f"Извлечён элемент с начала: '{item}'.")
    return item


def pop(queue):
    """Извлекает и возвращает элемент из конца очереди. Возвращает None, если очередь пуста."""
    if not queue:
        print("Очередь пуста, невозможно извлечь элемент.")
        return None
    item = queue.pop()
    print(f"Извлечён элемент с конца: '{item}'.")
    return item


def append_left(queue, item):
    """Добавляет элемент в начало очереди."""
    queue.appendleft(item)
    print(f"Добавлен элемент в начало очереди: '{item}'.")


def is_empty(queue):
    """Проверяет, пуста ли очередь."""
    return len(queue) == 0


def queue_size(queue):
    """Возвращает количество элементов в очереди."""
    return len(queue)


def display_queue(queue):
    """Отображает текущее состояние очереди."""
    if is_empty(queue):
        print("Очередь пуста.")
    else:
        print(f"Текущая очередь: {list(queue)}.")


def demonstrate_queue_operations():
    """Демонстрирует основные операции очереди."""
    print("\n" + "=" * 60)
    print("Демонстрация основных операций")
    print("=" * 60)

    queue = create_deque()
    print("Создана новая очередь.")
    display_queue(queue)

    # Добавляем элементы в очередь
    print("\n--- Добавление элементов в очередь ---")
    elements = ["Первый", "Второй", "Третий"]
    for element in elements:
        enqueue(queue, element)
    display_queue(queue)

    # Извлекаем элементы из очереди
    print("\n--- Извлечение элементов из очереди ---")
    while not is_empty(queue):
        dequeue(queue)
        display_queue(queue)

    # Попытка извлечь из пустой очереди
    print("\n--- Попытка извлечь из пустой очереди ---")
    dequeue(queue)
    display_queue(queue)


def demonstrate_extended_operations():
    """Демонстрирует расширенные опции с очередью."""
    print("\n" + "=" * 60)
    print("Демонстрация расширенных операций")
    print("=" * 60)

    queue = create_deque()
    print("Создана новая очередь")
    display_queue(queue)

    # Добавляем элементы в конец очереди
    print("\n--- Добавляем элементы в конец очереди ---")
    for i in range(1, 4):
        enqueue(queue, f"Элемент_{i}")
    display_queue(queue)

    # Добавляем элементы в начало
    print("\n--- Добавляем элементы в начало очереди ---")
    append_left(queue, "Специальный_элемент")
    append_left(queue, "Приоритетный_элемент")
    display_queue(queue)

    # Извлекаем элементы с конца
    print("\n--- Извлекаем элементы с конца (pop) ---")
    last_item = pop(queue)
    print(f"Извлечённый элемент с конца очереди: {last_item}")
    display_queue(queue)

    # Извлекаем элементы с начала очереди
    print("\n--- Извлекаем элемент с начала (dequeue) ---")
    first_item = dequeue(queue)
    print(f"Извлечённый элемент с начала очереди: {first_item}")
    display_queue(queue)

    # Смешанные операции
    print("\n--- Смешанные операции ---")
    append_left(queue, "Новый_в_начало")
    enqueue(queue, "Новый_в_конец")
    display_queue(queue)

    # Извлекаем по одному с разных сторон
    print("\n--- Попеременное извлечение с разных сторон ---")
    dequeue(queue)  # с начала
    pop(queue)  # с конца
    display_queue(queue)

    # Очищаем очередь
    print("\n--- Очистка очереди ---")
    while not is_empty(queue):
        dequeue(queue)
    display_queue(queue)


if __name__ == "__main__":
    demonstrate_queue_operations()
    demonstrate_extended_operations()
    print("-" * 90)
