'''Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.'''


class Car:
    def __init__(self, car_name):
        self.speed = 0
        self.color = None
        self.name = car_name
        self.is_police = False

    def go(self):
        print('Car is going.')

    def stop(self):
        print('Car has stopped.')

    def turn(self, direction):
        print('Car has turned', direction)

    def show_speed(self):
        print('Your speed is:', self.speed)


class TownCar(Car):
    def show_speed(self):
        super(TownCar, self).show_speed()
        if self.speed > 60:
            print('Above speed limit!')


class WorkCar(Car):
    def show_speed(self):
        super(WorkCar, self).show_speed()
        if self.speed > 40:
            print('Above speed limit!')


class PoliceCar(Car):
    def __init__(self, car_name):
        super(PoliceCar, self).__init__(Car)
        self.is_police = True


my_car = PoliceCar('Ford')
print(my_car.is_police)

