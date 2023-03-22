# https://python-course.readthedocs.io/projects/elementary/en/latest/lessons/18-pygame.html

import pygame
import sys
from pygame.color import THECOLORS

pygame.init()

screen = pygame.display.set_mode((1200, 800))
screen.fill(THECOLORS['orange'])

font = pygame.font.SysFont('couriernew', 40)
text = font.render(str('HELLO'), True, THECOLORS['green'])
screen.blit(text, (50, 50))

r_1 = pygame.Rect(200, 50, 100, 100)
r_2 = pygame.Rect(100, 150, 300, 100)
r_3 = pygame.Rect(600, 50, 100, 100)
r_4 = pygame.Rect(500, 150, 300, 100)
r_5 = pygame.Rect(200, 250, 500, 100)
r_6 = pygame.Rect(300, 350, 300, 100)
r_7 = pygame.Rect(400, 450, 100, 100)

pygame.draw.rect(screen, (188, 143, 143), r_1, 0)
pygame.draw.rect(screen, (188, 143, 143), r_2, 0)
pygame.draw.rect(screen, (188, 143, 143), r_3, 0)
pygame.draw.rect(screen, (188, 143, 143), r_4, 0)
pygame.draw.rect(screen, (188, 143, 143), r_5, 0)
pygame.draw.rect(screen, (188, 143, 143), r_6, 0)
pygame.draw.rect(screen, (188, 143, 143), r_7, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
