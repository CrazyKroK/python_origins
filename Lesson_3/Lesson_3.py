# Именные функции

# MAX
# print(max(1, 2, 3))
# print(max('zz', 'aaa'))
# my_var = ['zz', 'aaa', 'qweqwe']
# print(max(my_var, key=len))  # В качестве ключа для функции указываем len. В этом случае функция max выберет самый
# длинный элемент. len нужно указать без круглых скобок, так как мы не вызываем функцию len, а ссылаемся н нее. Если мы
# не укажем ключ, то max, будет сравнивать элементы листа по цифровой кодировке буквенных значений ascii.

# ROUND
# print(round(1.12345, 2))

# ENUMERATE
# for i, val in enumerate(['a', 'b', 'c'], start=1):
#     print(i, val)

# # СВОИ ФУНКЦИИ
# def qwe():  # Определение функции
#     print('qweqwe!')
#
#
# qwe()

# def say_hello(x):  # В эту функцию мы зашили аргумент x. Без определения переменной функция не запустится.
#     print('Hello', x)
#
#
# say_hello('Ivan')

# Среднее число
# def average(numbers):
#     result = (sum(numbers) / len(numbers))
#     return result
#
#
# out = average([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(out)

# def qwe(t):
#     pass  # Заглушка. Функция будет выдавать none, но не будет ронять систему. Можно дописать потом.
#
#
# print(qwe(600))

# ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ
# x = 100  # Глобальная переменная
#
#
# def test():  # Переменная x = 10 создалась только в рамках функции
#     x = 10
#
#
# test()
# print(x)  # Выдаст 100

# x = 100  # Глобальная переменная
#
#
# def test():  # Переменная x = 10 создалась только в рамках функции
#     global x  # но, мы сказали, что переменная глобальная, НО ТАК ДЕЛАТЬ НЕ СТОИТ
#     x = 10
#
#
# test()
# print(x)  # Выдаст 10

# x = 100
#
#
# def test(y):  # Вот так делать нужно
#     y = y + 1
#     return y
#
#
# x = test(x)
# print(x)

# АРГУМЕНТЫ
# def my_func(name, surname='Guest'):
#     print(name, surname)
#
#
# my_func('Ivan', 'Ivanov')  # Если мы не передадим второй аргумент (фамилия), то функция не упадет, а будет
# использовать дефолтное значение Guest

# def my_func(name, *args):  # В переменную agrs записываются все аргументы со второго. Используется, если мы
# не знаем сколько аргументов. Эту переменную принято называть args
#     print(name, args)
#
#
# my_func('Ivan', 10, 10, 10)

# def my_func(name, age, surname):
#     print(name, surname, age)
#
#
# my_func(age=50, name='Ivan', surname='Ivanov')

# def my_func(name, **kwargs):  # Создает словарь с указанными ключами. Используется, если неизвестно сколько будет
# с ключами. Принято называть kwargs
#     print(name, kwargs)
#
#
# my_func(age=50, name='Ivan', surname='Ivanov')

# ZIP
# names = ['Kirill', 'Vika', 'Oleg']
# ages = [17, 45, 55]
# print(list(zip(names, ages)))
#
# for name, age in zip(names, ages):
#     print(name, age)

# MAP
# def my_pow(x):
#     return x ** 2
#
#
# data = [1, 2, 3, 4]
# result = list(map(my_pow, data))  # map применяет функцию к каждому итерабельному объекту
# print(result)

# FILTER
# def my_filter(x):
#     return x > 0
#
#
# data = [-1, -2, 3, 4]
# result = list(filter(my_filter, data))  # фильтрует данные по указанной функции
# print(result)

# АНОНИМНАЯ ЛЯМБДА ФУНКЦИЯ
# data = [1, 2, 3, 4]
# result = list(map(lambda x: x ** 2, data))
# print(result)

# data = [-1, -2, 3, 4]
# result = list(filter(lambda x: x > 0, data))
# print(result)

# RANGE
# print(range(10))
# for i in range(5, 10, 2):  # Используется для определения диапазона. start, stop, step
#     print(i)

