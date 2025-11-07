"""                                1. Работа с файлами

                                    Работа с текстовыми файлами.

    В этом модуле мы будем изучать полезные технологии, нужны каждому программисту:

        ¤ Работу с разными видами файлов.
        ¤ Регулярные выражения.
        ¤ Полезные библиотеки.
        ¤ Всё, что упростит мне жизнь и разработку в будущем.

    Начнём мы с работы с текстовым файлами.

    В Python работа с текстовыми файлами осуществляется с помощью встроенных функций и методов.

    Вот основные шаги для работы с текстовыми файлами в Python:

        1. Открытие файла:

f = open("path/to/file", "filemode", encoding="utf-8")

    Для открытия файла используются функция open(). Она принимает два аргумента - имя файла и режим открытия.
Режим открытия "filemode" может быть "r" (чтение), "w" (запись), "a" (добавление/дозапись), "x" (создание и
запись), и другие.

    Создадим файл и запишем в него строку (с режимом "w" текст запишется в уже существующий файл, если он
создан, в противном случае файл создаётся):
"""

f = open("test.txt", "w")

# Запишем в файл строку
f.write("This is a test string")

# Обязательно нужно закрыть файл иначе он будет заблокирован ОС
f.close()

"""
    Запустим данный код. Рядом с исполняемым файлом в той же папке должен появится test.txt.

    Теперь откроем файл на чтение и считаем из него данные.
"""

f = open("test.txt", "r")
data = f.read()
print(data)
# Обязательно закрываем файл
f.close()

"""
Повторим код с другой строкой и увидим, что старые данные стёрлись и записались новые:
"""

f = open("test.txt", "w")
f.write("This is a ANOTHER string\n", )
f.close()

f = open("test.txt", "r")
data = f.read()
print(data)
f.close()

"""
Если мы хотим ДОЗАПИСАТЬ данные, используем режим "a":
"""

f = open("test.txt", "a")
f.write("This is a test string\n")
f.close()

f = open("test.txt", "r")
data = f.read()
print(data)
f.close()

"""
Для корректной работы с русским текстом добавляем параметр encoding="utf-8":
"""

f = open("test.txt", "w", encoding="utf-8")
f.write("Hello, Русский текст!\n")
f.close()

f = open("test.txt", "r", encoding="utf-8")
print(f.read())
f.close()

"""
                                     Чтение и запись построчно.

    Допустим, нам нужно записать список данных в столбик:
"""

f = open("test_1.txt", "w", encoding="utf-8") # Открываем файл на дозапись
sequence = ["Первая строка\n", "Вторая строка\n", "Третья строка\n"]
f.writelines(sequence) # Берёт строки из sequence и записывает в файл (без переносов)
f.close()

f = open("test_1.txt", "r", encoding="utf-8")
# data = f.readlines()
data = [i for i in f.readlines()]
for line in data:
    print(line.rstrip())
# data = f.readlines()
# for line in data:
#     print(line.rstrip())
#print(data)
f.close()

"""
    Для тестирования следующего кода создадим файл numbers.txt и запишем туда последовательность чисел,
каждое с новой строки:
"""

f = open("numbers.txt", "w", encoding="utf-8")
seq = [
    "1\n",
    "2\n",
    "3\n",
    "4\n",
    "5\n",
    "6\n",
    "7\n",
    "8\n",
    "9\n",
    "10\n"
]
f.writelines(seq)
f.close()

# f = open("numbers.txt", "r", encoding="utf-8")
# #data = f.readlines()
# # data = [int(i) for i in f.readlines()]
# # for line in data:
# #     print(line)
# data = list(map(int, f.readlines()))
# for line in data:
#     print(line)
# #print(data)
# f.close()

"""
                                     Менеджер контекста with.

    Если попробовать позапускать код выше без закрытия файла, то наткнёмся на проблемы - например, данные не
записались или файл не открывается повторно. Подобная проблема может возникнуть, если перед закрытием файла
произошла ошибка и код остановился. Тогда в идеале, чтобы это избежать-нам нужно составить следующий
алгоритм.
"""

# try:
#     somefile = open("hello.txt", "w")
#     try:
#         somefile.write("Hello, world!\n")
#     except Exception as e: # вдруг возникнет какая-то ошибка
#         print(e)
#     finally:
#         somefile.close() # файл закроется в любом случае
# except Exception as ex:
#     print(ex)

"""
    По такому же принципу работает менеджер контекста. Менеджер контекста неявно вызывает закрытие файла
после работы. Что освобождает нас от забот о том, закрыли ли мы файл или нет. Закрытие файла происходит при
любом стечении обстоятельств, даже если внутри with будет ошибка.
"""

with open("numbers.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip())

"""
    Можно даже использовать его вложенной:
"""

# копирование содержимого файла
with open("test_1.txt", "r", encoding="utf-8") as ONE:
    with open("test_new.txt", "w", encoding="utf-8") as SECOND:
        for line in ONE:
            SECOND.write(line)

with open("test_new.txt", "r", encoding="utf-8") as SECOND:
    for line in SECOND:
        print(line.rstrip())

