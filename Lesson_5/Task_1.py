''' Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.'''

file = open("Task_1.txt", "w")

my_list = []
while True:
    my_str = input('Введите данные (для окончания программы введите пустую строку): ')
    my_list.append(my_str)
    my_list.append('\n')
    if my_str == '':
        break

print(my_list)
file.writelines(my_list)
file.close()
