# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_division(x, y):
    if y == 0:
        print('На ноль делить нельзя')
    else:
        result = x / y
        return round(float(result), 2)


a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))
print(my_division(a, b))
