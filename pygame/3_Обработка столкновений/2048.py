import random
import sys

import pygame
from pygame.color import THECOLORS

pygame.init()

WIDTH = 640
HEIGHT = 450

screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Game:

    def __init__(self):

        self.cell_pos_dict = {1: None,  # Хранит информацию о том, какие клетки находятся в ячейках
                              2: None,
                              3: None,
                              4: None,
                              5: None,
                              6: None,
                              7: None,
                              8: None,
                              9: None,
                              10: None,
                              11: None,
                              12: None,
                              13: None,
                              14: None,
                              15: None,
                              16: None}

        self.coord_dict = {1: [10, 10],
                           2: [120, 10],
                           3: [230, 10],
                           4: [340, 10],
                           5: [10, 120],
                           6: [120, 120],
                           7: [230, 120],
                           8: [340, 120],
                           9: [10, 230],
                           10: [120, 230],
                           11: [230, 230],
                           12: [340, 230],
                           13: [10, 340],
                           14: [120, 340],
                           15: [230, 340],
                           16: [340, 340]}

    @staticmethod
    def cell_pos_calc(coord_x, coord_y):  # считает ключ для coord_dict из координат
        result = (coord_x - 10) / 110 + 4 * (coord_y - 10) / 110 + 1
        return result


class ScreenStruck:

    def __init__(self):
        self.line_length = 450
        self.line_width = 10
        self.line_pos = 0
        self.line_color = THECOLORS['azure3']

    def draw(self):
        while True:
            lines_vert = pygame.Rect(self.line_pos, 0, self.line_width, self.line_length)
            lines_hor = pygame.Rect(0, self.line_pos, self.line_length, self.line_width)
            pygame.draw.rect(screen, self.line_color, lines_vert, 0)
            pygame.draw.rect(screen, self.line_color, lines_hor, 0)
            if self.line_pos < 440:
                self.line_pos += 110
            else:
                self.line_pos = 0
                break


class Cell:

    def __init__(self, name):

        self.name = name

        self.cell_width = 100

        # self.color_cell = THECOLORS['bisque2']
        self.color_cell = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))  # временно
        self.color_background = THECOLORS['azure2']
        self.font = pygame.font.SysFont('calibri', 120, True)
        self.font_color = THECOLORS['gray29']

        self.text_pos = None
        self.cell_form = None
        self.text_number = None

        check = 0
        for key, val in game.cell_pos_dict.items():
            if val:
                check += 1
        if check + 1 != move_cycle:
            print()

        new_cell_check = False
        while new_cell_check is False:
            self.cell_pos_key_try = random.randint(1, 16)
            if game.cell_pos_dict[self.cell_pos_key_try] is None:
                self.cell_pos_key = self.cell_pos_key_try
                new_cell_check = True

        self.cell_pos = game.coord_dict[self.cell_pos_key]
        self.number = random.randrange(2, 5, 2)
        self.pos_move = None

    def draw(self):
        self.text_pos = (self.cell_pos[0] + 18, self.cell_pos[1])

        self.cell_form = pygame.Rect(self.cell_pos, (self.cell_width, self.cell_width))
        pygame.draw.rect(screen, self.color_cell, self.cell_form, 0)

        self.text_number = self.font.render(str(self.number), True, self.font_color)
        screen.blit(self.text_number, self.text_pos)

        self.cell_pos_key = game.cell_pos_calc(self.cell_pos[0], self.cell_pos[1])
        game.cell_pos_dict[cell.cell_pos_key] = self.name  # Записывает имя клетки в cell_pos

    def move_left(self):
        game.cell_pos_dict[self.cell_pos_key] = None  # Обнуляет имя клетки в cell_pos

        pygame.draw.rect(screen, self.color_background, self.cell_form, 0)
        self.pos_move = 4 * (self.cell_pos[1] - 10) / 110 + 1  # считает ключ для крайней левой позиции в coord_dict
        if game.cell_pos_dict[self.pos_move] is None or game.cell_pos_dict[self.pos_move] == self.name:
            self.cell_pos[0] = 10
        elif game.cell_pos_dict[self.pos_move + 1] is None or game.cell_pos_dict[self.pos_move + 1] == self.name:
            self.cell_pos[0] = 120
        elif game.cell_pos_dict[self.pos_move + 2] is None or game.cell_pos_dict[self.pos_move + 2] == self.name:
            self.cell_pos[0] = 230

        self.cell_pos_key = game.cell_pos_calc(self.cell_pos[0], self.cell_pos[1])
        game.cell_pos_dict[self.cell_pos_key] = self.name  # Записывает имя клетки в cell_pos
        self.cell_form = pygame.Rect(self.cell_pos, (self.cell_width, self.cell_width))
        pygame.draw.rect(screen, self.color_cell, self.cell_form, 0)

    def move_right(self):
        game.cell_pos_dict[self.cell_pos_key] = None  # Обнуляет имя клетки в cell_pos

        pygame.draw.rect(screen, self.color_background, self.cell_form, 0)
        self.pos_move = 4 * (self.cell_pos[1] - 10) / 110 + 4  # считает ключ для крайней правой позиции в coord_dict
        if game.cell_pos_dict[self.pos_move] is None or game.cell_pos_dict[self.pos_move] == self.name:
            self.cell_pos[0] = 340
        elif game.cell_pos_dict[self.pos_move - 1] is None or game.cell_pos_dict[self.pos_move - 1] == self.name:
            self.cell_pos[0] = 230
        elif game.cell_pos_dict[self.pos_move - 2] is None or game.cell_pos_dict[self.pos_move - 2] == self.name:
            self.cell_pos[0] = 120

        self.cell_pos_key = game.cell_pos_calc(self.cell_pos[0], self.cell_pos[1])
        game.cell_pos_dict[self.cell_pos_key] = self.name  # Записывает имя клетки в cell_pos
        self.cell_form = pygame.Rect(self.cell_pos, (self.cell_width, self.cell_width))
        pygame.draw.rect(screen, self.color_cell, self.cell_form, 0)

    def move_up(self):
        game.cell_pos_dict[self.cell_pos_key] = None  # Обнуляет имя клетки в cell_pos

        pygame.draw.rect(screen, self.color_background, self.cell_form, 0)
        self.pos_move = (self.cell_pos[0] - 10) / 110 + 1  # считает ключ для крайней верхней позиции в coord_dict
        if game.cell_pos_dict[self.pos_move] is None or game.cell_pos_dict[self.pos_move] == self.name:
            self.cell_pos[1] = 10
        elif game.cell_pos_dict[self.pos_move + 4] is None or game.cell_pos_dict[self.pos_move + 4] == self.name:
            self.cell_pos[1] = 120
        elif game.cell_pos_dict[self.pos_move + 8] is None or game.cell_pos_dict[self.pos_move + 8] == self.name:
            self.cell_pos[1] = 230

        self.cell_pos_key = game.cell_pos_calc(self.cell_pos[0], self.cell_pos[1])
        game.cell_pos_dict[self.cell_pos_key] = self.name  # Записывает имя клетки в cell_pos
        self.cell_form = pygame.Rect(self.cell_pos, (self.cell_width, self.cell_width))
        pygame.draw.rect(screen, self.color_cell, self.cell_form, 0)

    def move_down(self):
        game.cell_pos_dict[self.cell_pos_key] = None  # Обнуляет имя клетки в cell_pos

        pygame.draw.rect(screen, self.color_background, self.cell_form, 0)
        self.pos_move = (self.cell_pos[0] - 10) / 110 + 13  # считает ключ для крайней нижней позиции в coord_dict
        if game.cell_pos_dict[self.pos_move] is None or game.cell_pos_dict[self.pos_move] == self.name:
            self.cell_pos[1] = 340
        elif game.cell_pos_dict[self.pos_move - 4] is None or game.cell_pos_dict[self.pos_move - 4] == self.name:
            self.cell_pos[1] = 230
        elif game.cell_pos_dict[self.pos_move - 8] is None or game.cell_pos_dict[self.pos_move - 8] == self.name:
            self.cell_pos[1] = 120

        self.cell_pos_key = game.cell_pos_calc(self.cell_pos[0], self.cell_pos[1])
        game.cell_pos_dict[self.cell_pos_key] = self.name  # Записывает имя клетки в cell_pos
        self.cell_form = pygame.Rect(self.cell_pos, (self.cell_width, self.cell_width))
        pygame.draw.rect(screen, self.color_cell, self.cell_form, 0)


game = Game()
screen_struct = ScreenStruck()
cells = []
cell_number = 1
move_cycle = 1
check_cycle = 0

while True:
    screen.fill(THECOLORS['azure2'])
    screen_struct.draw()

    if move_cycle > check_cycle:
        cell = Cell(cell_number)
        cells.append(cell)
        cell_number = cell_number + 1
        print(game.cell_pos_dict)

    check_cycle = move_cycle

    for cell in cells:
        cell.draw()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            move_cycle = move_cycle + 1
            if event.key == pygame.K_LEFT:
                for cell in cells:
                    cell.move_left()
            elif event.key == pygame.K_RIGHT:
                for cell in cells:
                    cell.move_right()
            elif event.key == pygame.K_UP:
                for cell in cells:
                    cell.move_up()
            elif event.key == pygame.K_DOWN:
                for cell in cells:
                    cell.move_down()

    pygame.display.flip()
    # pygame.time.delay(500)
