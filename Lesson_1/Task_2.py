# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

a = input('Введите время в секундах: ')
a = int(a)
hours = a // 3600
minutes = a % 3600 // 60
seconds = a % 60
if hours < 10:
    hours = ('0' + str(hours))
if minutes < 10:
    minutes = ('0' + str(minutes))
if seconds < 10:
    seconds = ('0' + str(seconds))
print(f'{hours}:{minutes}:{seconds}')
