'''Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).'''


class Worker:
    def __init__(self):
        self.name = None
        self.surname = None
        self.position = None
        self._income = {"wage": 100, "bonus": 50}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._income["wage"] + self._income["bonus"])


Kirill = Position()
Kirill.name = 'Kirill'
Kirill.surname = 'Gostev'
Kirill.get_full_name()
Kirill.get_total_income()
