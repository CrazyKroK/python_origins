import random
import sys

import pygame
from pygame.color import THECOLORS

pygame.init()

WIDTH = 800
HEIGHT = 450

screen = pygame.display.set_mode((WIDTH, HEIGHT))


class ScreenStruck:

    line_length = 450
    line_width = 10
    line_pos = 0
    line_color = THECOLORS['azure3']
    score = 0

    @classmethod
    def draw(cls):
        while True:
            lines_vert = pygame.Rect(cls.line_pos, 0, cls.line_width, cls.line_length)
            lines_hor = pygame.Rect(0, cls.line_pos, cls.line_length, cls.line_width)
            pygame.draw.rect(screen, cls.line_color, lines_vert, 0)
            pygame.draw.rect(screen, cls.line_color, lines_hor, 0)
            if cls.line_pos < 440:
                cls.line_pos += 110
            else:
                cls.line_pos = 0
                break

            screen.blit(pygame.font.SysFont('calibri', 40, bold=True).render('SCORE: ' + str(cls.score), True, THECOLORS['coral3']), (460, 10))


class Game:

    cell_pos_dict = {11: None, 12: None, 13: None, 14: None,  # Хранит клетки по ячейкам.
                     21: None, 22: None, 23: None, 24: None,
                     31: None, 32: None, 33: None, 34: None,
                     41: None, 42: None, 43: None, 44: None}

    color_dict = {2 ** 1: (255, 255, 255), 2 ** 2: (224, 224, 224), 2 ** 3: (160, 160, 160), 2 ** 4: (128, 128, 128),
                  2 ** 5: (204, 255, 204), 2 ** 6: (153, 255, 153), 2 ** 7: (51, 255, 51), 2 ** 8: (0, 204, 0),
                  2 ** 9: (229, 204, 255), 2 ** 10: (204, 153, 255), 2 ** 11: (178, 102, 255), 2 ** 12: (153, 51, 255),
                  2 ** 13: (255, 204, 204), 2 ** 14: (255, 153, 153), 2 ** 15: (255, 51, 51), 2 ** 16: (204, 0, 0)}

    # Хранит информацию о местоположении числа относительно клетки
    # (первые 2 цифры в списке) и размер шрифта (3 цифра). Подтягивается к числу, исходя из его длины.
    text_pos_dict = {1: [18, 0, 120], 2: [2, 10, 95], 3: [2, 22, 62], 4: [2, 27, 47], 5: [2, 33, 37]}

    direction_dict = {'Game.left': 1, 'Game.right': -1, 'Game.up': 10, 'Game.down': -10}  # содержит атрибуты для метода класса Cell (move_add).

    move_cycle = 1   # Две переменные, отвечающие за условие создания новой клетки в new_cell.
    check_cycle = 0  # После любого движения move_cycle увеличивается на 1, что является необходимым условием для создания клетки, далее check_cycle догоняет move_cycle.

    cell_number = None
    cell = None

    @classmethod
    def move_add_status(cls):
        result = False
        for value in cls.cell_pos_dict.values():
            if value is not None:
                if value.move_status is True or value.mult_status is True:
                    result = True
        return result

    @classmethod
    def game_over_check(cls):

        game_over = False
        none_count = 0
        neighbour_count = None

        # Блок проверяет, что все ячейки заняты.
        for value in cls.cell_pos_dict.values():
            if value is None:
                none_count += 1

        # Если все клетки заняты, то для каждой клетки блок проверяет совпадения значения клетки с правой или нижней.
        # Если такое совпадение есть, цикл прерывается и игра продолжается, если нет - game over.
        if none_count == 0:
            for value in cls.cell_pos_dict.values():
                if ((value.cell_pos % 10 < 4 and value.cell_number == cls.cell_pos_dict[value.cell_pos + 1].cell_number)
                        or (value.cell_pos // 10 < 4 and value.cell_number == cls.cell_pos_dict[value.cell_pos + 10].cell_number)):
                    neighbour_count = True
                    break
                else:
                    neighbour_count = False

        if neighbour_count is False:
            game_over = True
            screen.blit(pygame.font.SysFont('calibri', 120, bold=True).render('GAME OVER', True, THECOLORS['coral3']), (15, 165))  # Надпись Game over.
        return game_over

    @classmethod
    def new_cell(cls):
        if cls.move_cycle > cls.check_cycle:
            sequence = (2, 2, 2, 2, 2, 2, 2, 2, 2, 4)
            cls.cell_number = random.choice(sequence)
            cls.cell = Cell(cls.cell_number)

            cls.cell_pos_dict[cls.cell.cell_pos] = cls.cell
            cls.check_cycle = cls.move_cycle

    @staticmethod
    def from_pos_to_coord(pos):
        return [pos % 10 * 110 - 100, pos // 10 * 110 - 100]

    # 4 метода ниже используются для движения и сложения клеток в классе Cell (move_add). Нужная формула подтягивается по направлению и параметру order.
    @staticmethod
    def left(cell_pos, order):
        if order == 1:
            return cell_pos // 10 * 10 + 1
        elif order == 2:
            return cell_pos % 10 > 1

    @staticmethod
    def right(cell_pos, order):
        if order == 1:
            return cell_pos // 10 * 10 + 4
        elif order == 2:
            return cell_pos % 10 < 4

    @staticmethod
    def up(cell_pos, order):
        if order == 1:
            return cell_pos % 10 + 10
        elif order == 2:
            return cell_pos // 10 > 1

    @staticmethod
    def down(cell_pos, order):
        if order == 1:
            return cell_pos % 10 + 40
        elif order == 2:
            return cell_pos // 10 < 4


class Cell:

    def __init__(self, number):
        self.cell_number = number
        self.cell_width = 100

        self.color_cell = Game.color_dict[self.cell_number]
        self.color_background = THECOLORS['azure2']
        self.font = None
        self.font_color = THECOLORS['gray29']

        new_cell_check = False  # Блок проверяет можно ли создать новую клетку в ячейке cell_pos_dict и создает если можно.
        new_cell_count = 0
        while new_cell_check is False:
            new_cell_count += 1
            self.cell_pos_try = random.randint(1, 4) * 10 + random.randint(1, 4)
            if Game.cell_pos_dict[self.cell_pos_try] is None:
                self.cell_pos = self.cell_pos_try
                new_cell_check = True

        self.cell_pos_move = None
        self.cell_coord = Game.from_pos_to_coord(self.cell_pos)
        self.cell_form = None
        self.move_status = None
        self.mult_status = None

        self.text_pos = None
        self.text_number = None

    def draw(self):
        self.color_cell = Game.color_dict[self.cell_number]
        self.cell_form = pygame.Rect(self.cell_coord, (self.cell_width, self.cell_width))
        pygame.draw.rect(screen, self.color_cell, self.cell_form, 0)

        self.font = pygame.font.SysFont('calibri', Game.text_pos_dict[len(str(self.cell_number))][2], True)
        self.text_pos = (self.cell_coord[0] + Game.text_pos_dict[len(str(self.cell_number))][0], self.cell_coord[1] + Game.text_pos_dict[len(str(self.cell_number))][1])
        self.text_number = self.font.render(str(self.cell_number), True, self.font_color)
        screen.blit(self.text_number, self.text_pos)

    def move_add(self, direction):
        self.move_status = False  # Переменная меняется, если клетка только что передвинулась. Нужна для отслеживания условия для создания новых клеток.
        self.mult_status = False  # Переменная меняется, если клетка только что была сложена. Нужна для того, чтобы клетки не складывались паровозиком
        # А также для отслеживания условия для создания новых клеток.
        Game.move_cycle += 1

        Game.cell_pos_dict[self.cell_pos] = None  # Блок отвечает за движение.
        self.cell_pos_move = eval(direction)(self.cell_pos, 1)
        while Game.cell_pos_dict[self.cell_pos_move] is not None:
            self.cell_pos_move = self.cell_pos_move + Game.direction_dict[direction]
        else:
            if self.cell_pos == self.cell_pos_move:
                self.move_status = False
            else:
                self.move_status = True
            self.cell_pos = self.cell_pos_move

        # Блок отвечает за сложение. Условие в if разбито на 3 условия. Первое условие проверяет не занимает ли клетка крайнее положение.
        # Например, если клетка занимает крайнее левое положение, то левее нее не может быть клетки с которой она могла бы сложиться, по этому сложение для нее невозможно.
        # Второе условие совпадает ли номер клетки и номер следующей по вектору движения клетки.
        # Третье условие проверяет не была ли клетка только что сложено. Нужно для того, чтобы клетки не складывались паровозиком.
        if (eval(direction)(self.cell_pos, 2) and
                self.cell_number == Game.cell_pos_dict[self.cell_pos - Game.direction_dict[direction]].cell_number and
                Game.cell_pos_dict[self.cell_pos - Game.direction_dict[direction]].mult_status is False):
            Game.cell_pos_dict[self.cell_pos - Game.direction_dict[direction]] = None
            self.cell_pos = self.cell_pos - Game.direction_dict[direction]
            self.cell_number *= 2
            ScreenStruck.score += self.cell_number
            self.mult_status = True
        Game.cell_pos_dict[self.cell_pos] = cell
        self.cell_coord = Game.from_pos_to_coord(self.cell_pos)


while True:
    screen.fill(THECOLORS['azure2'])
    ScreenStruck.draw()
    if Game.move_add_status() is True or Game.move_cycle == 1:
        Game.new_cell()

    for cell in Game.cell_pos_dict.values():
        if cell is not None:
            cell.draw()

    Game.game_over_check()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if Game.game_over_check() is False:
            if event.type == pygame.KEYDOWN:  # Блок отвечает за движение клетки. В движении вправо и вниз словари итерируются с конца, чтобы не ломался порядок движения.
                if event.key == pygame.K_LEFT:
                    for cell in Game.cell_pos_dict.values():
                        if cell is not None:
                            cell.move_add('Game.left')
                elif event.key == pygame.K_RIGHT:
                    for cell in dict(reversed(list(Game.cell_pos_dict.items()))).values():
                        if cell is not None:
                            cell.move_add('Game.right')
                elif event.key == pygame.K_UP:
                    for cell in Game.cell_pos_dict.values():
                        if cell is not None:
                            cell.move_add('Game.up')
                elif event.key == pygame.K_DOWN:
                    for cell in dict(reversed(list(Game.cell_pos_dict.items()))).values():
                        if cell is not None:
                            cell.move_add('Game.down')

    pygame.display.flip()
