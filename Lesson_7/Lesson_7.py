# class Car:
#     def __init__(self):
#         self.modules = []
#         self.fuel_per_km = 5
#
#     def __add__(self, other):
#         self.modules.append(other)
#
#     def __str__(self):
#         return 'Авто с модулями: ' + ' ,'.join(self.modules)
#
#     def __del__(self):
#         print('Объект удален')
#
#     def __setattr__(self, key, value):
#         # super().__setattr__(key, value)
#         self.__dict__[key] = value
#         print('Добавлен ключ', key, 'со значением', value)
#
#     def __getitem__(self, item):
#         return self.modules[item]  # Позволяет обращаться к объектам внутри списка modules напрямую (car[2]).
#
#     def __call__(self, price=None):
#         print('Машина:', self.model, 'модули:', self.modules, 'Цена:', price)  # Позволяет вызвать экземпляр класса
#         как функцию
#
#     def __eq__(self, other):
#         return self.fuel_per_km == other  # Сравнивает (==) заданное значение с введенным


# car = Car()
# a = 'теплый руль'
# b = 'теплое сиденье'
# c = 'панорама'
# car + a
# car + b
# car + c
# car.model = 'BMW'
# print(car.modules[2])
# print(car[2])
# car(1000)
# print(car == 6)

# ИНТЕРФЕЙСЫ

# from abc import ABC, abstractmethod
#
#
# class MyABCClass(ABC):
#     @abstractmethod  # Заставляет описывать или переопределять метод, описанный ниже в дочерних классах.
#                      # Без этого ошибка.
#     def my_method(self):
#         pass
#
#
# class MyClass(MyABCClass):
#
#     def my_method(self):
#         pass
#
#
# mc = MyClass()

# ИТЕРАТОРЫ
#
# for i in [1, 2, 3, 4, 5]:
#     print(i)
#
#
# class Iterator:
#     def __init__(self):
#         self.i = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.i = self.i + 1
#         if self.i <= 5:
#             return self.i
#         else:
#             raise StopIteration
#
#
# qwe = Iterator()
# for i in qwe:
#     print(i)


# ДЕКОРАТОР

# class Human:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self._age = age
#
#     @property  # Позволяет маскировать функцию под атрибут
#     def age(self):
#         return self._age
#
#
# human = Human('Ivan', 'Ivanov', 20)
# print(human.age)


# КОМПОЗИЦИЯ

class WinDoor:
    def __init__(self, wd_len, wd_wid):
        self.square = wd_len * wd_wid


class Room:
    def __init__(self, l1, l2, h):
        self.square = 2 * h * (l1 + l2)
        self.wd = []

    def add_windoor(self, wd_len, wd_wid):
        self.wd.append(WinDoor(wd_len, wd_wid))  # Композиция это когда мы собираем внутри одного класса
                                                 # экземпляры других классов

    def common_square(self):
        main_square = self.square
        for el in self.wd:
            main_square = main_square - el.square
        print(main_square)


r = Room(4, 5, 3)
print(r.square)
r.add_windoor(1, 2)
r.add_windoor(2, 2)
r.add_windoor(1, 1)
r.common_square()
