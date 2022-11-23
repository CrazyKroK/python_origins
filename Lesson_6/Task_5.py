'''Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.'''


class Stationery:
    def __init__(self, title):
        self.stationery_title = title

    def draw(self):
        print('Запуск отрисовки!')


class Pen(Stationery):
    def draw(self):
        super(Pen, self).draw()
        print('Используется ручка!')


class Pencil(Stationery):
    def draw(self):
        super(Pencil, self).draw()
        print('Используется карандаш!')


class Handle(Stationery):
    def draw(self):
        super(Handle, self).draw()
        print('Используется маркер!')


pen_1 = Pen('Моя_ручка')
pen_1.draw()

pencil_1 = Pencil('Мой_карандаш')
pencil_1.draw()

handle_1 = Handle('Мой маркер')
handle_1.draw()
