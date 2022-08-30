'''
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить
только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''

from functools import reduce
from itertools import count

stop = int(input('Введите число, факториал от которого нужен: '))


def fact(a):
    list_a = [a]
    for el in list_a:
        ind = list_a.index(el)
        el = el - 1
        if el > 0:
            list_a.insert(ind + 1, el)
        if el == 0:
            break
    result = reduce(lambda b, c: b * c, list_a)
    return result


def gen_1():
    for el in count(1):
        yield fact(el)


x = 0
for i in gen_1():
    print('Factorial', x + 1, '-', i)
    if x == stop - 1:
        break
    x = x + 1
