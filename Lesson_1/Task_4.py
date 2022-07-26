# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

# number = input('Введите целое положительное число: ')
# number = int(number)
# number_a = number
# number_b = number // 10
# a = number_a % 10
# b = number_b % 10
#
# while number_b > 9 > a:
#     if a < b:
#         number_a = number_a // 10
#         a = number_a % 10
#         print(f'{number_a}, {a}, {number_b}, {b}')
#     else:
#         number_b = number_b // 10
#         b = number_b % 10
#         print(f'{number_a}, {a}, {number_b}, {b}')
# else:
#     if a > b:
#         print(a)
#     else:
#         print(b)

number = input('Введите целое положительное число: ')
number = int(number)
digit = number % 10
max_digit = 0
while number > 0 and digit < 9:
    if max_digit < digit:
        max_digit = digit
    number = number // 10
    digit = number % 10
else:
    print(max_digit)
