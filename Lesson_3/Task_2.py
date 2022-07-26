# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def personal_data(name, surname, yob):
    result = [name, surname, yob]
    return result


my_name = input('Введите имя: ')
my_surname = input('Введите фамилию: ')
my_yob = input('Введите год рождения: ')

# print(personal_data(my_name, my_surname, my_yob))

print(f'Имя: {personal_data(my_name, my_surname, my_yob)[0]}, Фамилия: {personal_data(my_name, my_surname, my_yob)[1]},'
      f'Год рождения: {personal_data(my_name, my_surname, my_yob)[2]}')

