'''Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
— одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.'''


from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self):
        self.size = input('Введите размер пальто: ')

    @property
    def fabric_consumption(self):
        return 'Расход ткани равен на пальто', int(self.size) / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self):
        self.height = input('Введите рост костюма: ')

    @property
    def fabric_consumption(self):
        return 'Расход ткани равен на костюм', int(self.height) * 2 + 0.3


coat = Coat()
print(coat.fabric_consumption)

suit = Suit()
print(suit.fabric_consumption)
