# class DBconnection:
#
#     def connect(self):
#         print('connecting!')
#
#     @staticmethod  # Позволяет обращаться к методу не создавая экземпляр класса
#     def select():
#         print('selecting')
#
#     @classmethod  # Позволяет обращаться напрямую к методам класса.
#     def my_method(cls, param):
#         print(cls.connect(self=db), param)


# DBconnection.select()
# db = DBconnection()
# db.my_method(44)

# class Customer:
#     """Это класс Customer. Его описание."""
#     def __init__(self, name, phone, address):
#         self.name = name
#         self.phone = phone
#         self.address = address
#
#
# john = Customer('John', 123, 'USA')
# print(john.__dict__)  # Выводит значения всех атрибутов в виде словаря.
# print(john.__doc__)  # Выводит описание класса.
# print(john.__class__.__name__)  # Вызывает объект, дает возможность посмотреть атрибуты объекта, например,
#                                 # назваение класса.
# print(john.__class__.__module__)  # Название модуля, из которого подгружается класс.
#
# Свои исключения можно создавать через класс Exception
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


input_data = input('Введите положительное число: ')

try:
    input_data = int(input_data)
    if input_data < 0:
        raise OwnError('Вы ввели отрицательное число!')
except OwnError:
    print('Отрицательное число!')

# Для того чтобы скачать и установить библиотеку пишем в терминале pip install название библиотеки.
# Описание библиотек смотрим на сайте pip
# Virtualenv виртуальное окружение используется для создания
# изолированного рабочего стола с нужными версиями библиотек
