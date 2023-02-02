'''Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт.'''

import time


class TrafficLight:
    def __init__(self):
        self._colour = None

    def running(self):
        cycle_count = 0
        cycle_amount = int(input('Введите количество циклов работы светофора: '))
        while cycle_count < cycle_amount:
            self._colour = 'red'
            print(self._colour)
            time.sleep(7)
            self._colour = 'yellow'
            print(self._colour)
            time.sleep(2)
            self._colour = 'green'
            print(self._colour)
            time.sleep(5)
            cycle_count = cycle_count + 1


my_traffic_light = TrafficLight()
my_traffic_light.running()
