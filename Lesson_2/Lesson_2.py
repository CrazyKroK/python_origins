# a = None
# print(type(a))

# a = -65
# print(abs(a))

# 5 & 3 = 1 Побитовое умножение/логическое и: 0101 * 0011 = 0001

# 5 | 3 = 7 Побитовое сложение/логическое или: 0101 + 0011 = 0111
# По непонятной мне причине в побитовом сложении 1 + 1 = 1, по этому при сложении первых единиц получается 1

# 5 ^ 3 = 6 Логическое исключающее или: 0101 ^ 0011 = 0110. Сравнивает побитово 2 числа.
# Единица там, где биты различаются, ноль - где совпадают.

# 6 >> 1 = 3 Побитовый сдвиг вправо/деление. Первый член делится на 2 в степени второго члена (6 / 2 = 3).

# 6 << 1 = 12 Побитовый сдвиг влево/умножение. Первый член умножается на 2 в степени второго члена

# print(int('0101', 2)) Второй аргумнет определяет систему исчисления (от 2 до 36). Ответ 6.

# print(bin(17)) Переводит в двоичную систему исчисления. oct - восьмиричная, hex - шерстнадцатиричная.


# СРЕЗ SLICE
# a = 'Анастасия'
# print(a[7:2:-1]) Срез/slice. [start:stop:step] Первый элемент идет с индексом 0.
# При step -1 - перевернет слово, а start и stop поменяются местами.
# Значение start включается, stop исключается.

# print(len(a)) Считает длинну строки.

# print(a[4]) Вызывает символ по иденксу.

# val = 'gostev_kirill@mail.ru'

# print(val.split('@')) Разделяет по символу.

# val = 'Кирилл Гостев 27'
# name, surname, age = val.split()
# print(name)

# my_list = ['Кирилл', 'Гостев']
# print('_'.join(my_list))  # Кирилл_Гостев

# a = 'анастасия пЕТРовна'
# print(a.title())  # Все слова с большой буквы, остальные маленькие
# print(a.lower())  # маленькие буквы
# print(a.upper())  # большие буквы
# print(a.capitalize())  # первые слово с большой буквы, остальные маленькие
# print(a.istitle())  # Проверка если с больших букв
# print('А' in a)  # Проверка на наличие букв
# print(a.count('а'))
# print(a.find('а'))  # если не найдено возвращает -1

# СПИСОК LIST
# a = ['qwe', 544, 2.0]
# print(a[2])
# [start:stop:step]
# print(a[2:])
# a.append(888)  # добавить в конец
# print(a)
# a.insert(2, 'fsd')  # вставляет по индексу
# print(a)
# b = a.pop()  # вырезает любой элемент по индексу, вставляет в буффер
# print(a)
# print(b)
# a.reverse()  # перевернуть
# print(a)
# print(a.index('qwe'))
# print('qwe' in a)  # Проверка на наличие элемента
# print('q' in a[0])  # Проверка на наличие символа в элементе

# IS сравнивает переменные по ячейкам памяти
# a = 10
# b = 10
# print(a is b)
# print(id(a))  # узнать ячейку памяти
# print(id(b))
# list с одинаковыми элементами всегда занимают разные ячейки памяти так как списки изменяемы

# a = ['asd']
# b = a
# b.append('eds')
# print(a)
# в случае исполнения кода в функции в переменной а тоже будут 2 элемента, т.к. list - изменяемая переменная
# чтобы этого избежать используем метод .copy
# a = ['asd']
# b = a.copy()
# b.append('eds')
# print(a)

# a = ['asd', [1, 2, 3]]
# b = a.copy()
# b[1].append('qwe')
# print(a)
# в этом случая при копировании списка для b создалась новая ячейка памяти, но для списка b[1] она не изменилась
# чтобы этого избежать вызываем модуль copy и используем метод deepcopy

# import copy
# a = ['asd', [1, 2, 3]]
# b = copy.deepcopy(a)
# b[1].append(4)
# print(a)


# КОРТЕЖ tuple это неизменяемый list
# a = (2, 3, 5)
# print(type(a))


# МНОЖЕСТО set
# a = {1, 3, 5}
# print(a)
# print(type(a))

# a = {1, 2, 3, 1, 3, 4, 6, 5}  # множество берет уникальные элементы. Может поменять порядок
# print(a)

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a | b)  # множества можно сложить
# print(a - b)  # множества можно вычитать из друг друга (уникальные элементы вычитаемого множества пропадут
# print(a == b)  # множества можно сравнить
# print(a & b)  # у множеств можно искать пересечения
# print(a ^ b)  # все кроме пересечений
# a.remove(3)  # удаляет элемент по значению (не по индексу). При отсутствии элемента выдает ошибку
# a.discard(5)  # удаляет элемент по значению (не по индексу). При отсутствии элемента НЕ выдает ошибку

# СЛОВАРЬ dict
# a = {'name': 'Fedor', 'surname': 'Ivanov'}
# print(a['name'])  # Выдаст ошибку если ключа нет
# print(a.get('street'))  # Выдаст None если ключа нет
# a['street'] = 'Green avenue'
# print(a)
# a.pop('name')  # вырезает значение по ключу
# a.popitem()  # вырезает последнее значение по ключу
# print(a.keys())
# print(a.values())
# print(a.items())


# Исключения
# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print('Делить на ноль нельзя')
#
# try:
#     print(int('asd'))
# except ValueError:
#     print('Не число')


# For проходится по элементам итерируемых переменных циклом. Создает переменную налету
# list_1 = ['a', 'b', 1, 2, 3]
# for elem in list_1:
#     print(elem)

# Можно присвоить элементам порядковый номер (по-умолчанию с 0, но задается любой)
# list_1 = ['a', 'b', 1, 2, 3]
# for i, elem in enumerate(list_1, start=1):
#     print(i, elem)

# a = {'name': 'Fedor', 'surname': 'Ivanov'}
# for key, value, in a.items():
#     print(key, value)

# ТЕРНАРНЫЙ ОПЕРАТОР if else в одной строке
# a = 5 if 9 > 5 else 0
# print(a)

# age = input('Введите возраст: ')
# print('Welcome' if int(age) >= 18 else 'No access')
