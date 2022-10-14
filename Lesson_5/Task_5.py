'''Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''

from random import randint


def multiple_replace(target_str, replace_values):
    for i, j in replace_values.items():
        target_str = target_str.replace(i, j)
    return target_str


dict_replacer = {"[": "", "]": "", ",": "", "'": ""}

numbers = []
step = 0
while True:
    a = randint(1, 100)
    numbers.append(a)
    step = step + 1
    if step > 19:
        break

file_input = open('Task_5.txt', 'w')
str_numbers = multiple_replace(str(numbers), dict_replacer)
file_input.write(str_numbers)
file_input.close()

file_output = open('Task_5.txt', 'r')
content = file_output.readlines()
str_content = multiple_replace(str(content), dict_replacer)
list_content = str_content.split()
file_output.close()

total_sum = 0
for b in list_content:
    total_sum = total_sum + int(b)

print(total_sum)
