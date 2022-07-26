# МОДУЛИ

# IMPORT способ импортирования целиком
# import My_module as mm
# mm.my_func(1, 2)
# mm.my_new_func(1, 2)

# FROM способ импортирования одной функции из модуля
# from My_module import my_func  # можно поставить * и тогда будут импортированы все функции из модуля
# my_func(1, 2)

# СИСТЕМНЫЕ МОДУЛИ

# import time
# print(time.time())  # Секунды с 1 января 1970 г.
# a = time.time()
# for i in range(10000):
#     pass
# b = time.time()
# print(b - a)  # способ подсчета времени, которое уходит на процесс

# import math  # математический модуль
# print(math.pi)
# print(math.floor(1.2))  # округление в большую сторону
# print(math.ceil(1.2))  # округление в меньшую сторону

# import sys  # системный модуль
# print(sys.path)

# import os  # системный модуль про директории
# print(os.getcwd())  # показывает текущую директорию
# print('\n'.join(os.listdir()))  # ИЗУЧИТЬ КАК УЗНАТЬ ПАПКА ИЛИ ФАЙЛ

# ГЕНЕРАТОРНЫЕ ВЫРАЖЕНИЯ НЕ ИСПОЛЬЗУЕТСЯ С КОРТЕЖЕМ
# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# new = [qwe + 1 for qwe in my_list if qwe % 2 == 0]
# print(new)

# my_dict = {el: el*2 for el in range(30)}
# print(my_dict)
#
# generator = (p * p for p in range(31))
# for i in generator:
#     print(i)

# RANDOM
# import random
# print(random.random())
# print(random.randint(1, 50))
# print(random.randrange(0, 50, 5))

# ГЕНЕРАТОР
# def generator_1():
#     for el in (10, 20, 30):
#         yield el  # выдает не значение, а логику, тем самым не загружает память всеми элементами кортежа
#         в этом и есть смысл генератора ИСПОЛЬЗУЕТСЯ С КОРТЕЖЕМ
#
#
# g = generator_1()
# for i in g:
#     print(i)

# FUNCTOOLS
# from functools import reduce, partial
#
#
# def my_f(num1, num2):
#     return num1 + num2
#
#
# print(reduce(my_f, [10, 20, 30]))  # подставляет в функцию 10 и 20, а потом результат от первой итерации и 30
#
#
# def new_f(a, b):
#     return a ** b
#
#
# new_f_2 = partial(new_f, 2)  # позволяет заложить в функцию первый аргумент, завернуть ее в другую функцию,
# а потом заложить второй аргумент уже в новую функцию
# print(new_f_2(4))

# ITERTOOLS
# from itertools import count, cycle
# count(start=0, step=1)  # бесконечная последовательность
# c = 0
# for i in cycle(['green', 'red', 'yellow']):
#     print(i)
#     c = c + 1
#     if c > 10:
#         break
