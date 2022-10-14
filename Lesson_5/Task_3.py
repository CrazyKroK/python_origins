'''Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.'''

my_f = open("Task_3.txt", "r")
content = my_f.readlines()
print(content, '\n')

lines = len(content)
total_wage = 0
print('Сотрудники с окладом менее 30000 руб.:')
for elem in content:
    surname, wage = elem.split()
    total_wage = total_wage + int(wage)
    if int(wage) < 30000:
        print(surname, wage)

aver_wage = total_wage / lines
print('\nСредний оклад равен:', aver_wage)

my_f.close()
