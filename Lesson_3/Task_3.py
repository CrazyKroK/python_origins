# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов

def my_func(a, b, c):
    result = a + b + c - min(a, b, c)
    return result


x = int(input('Введите 1-ое число: '))
y = int(input('Введите 2-ое число: '))
z = int(input('Введите 3-е число: '))

print(my_func(x, y, z))
