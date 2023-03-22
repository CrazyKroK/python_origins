import pygame
import sys
from pygame.color import THECOLORS

pygame.init()

screen = pygame.display.set_mode((1200, 800))
screen.fill(THECOLORS['cadetblue1'])

stick = pygame.Rect(90, 90, 10, 710)
flag = [(100, 100), (1100, 100), (900, 300), (1100, 500), (100, 500)]

pygame.draw.rect(screen, (THECOLORS['black']), stick, 0)
pygame.draw.polygon(screen, (THECOLORS['white']), flag, 0)

pygame.draw.circle(screen, (THECOLORS['blue']), (375, 225), 75, 0)
pygame.draw.circle(screen, (THECOLORS['black']), (525, 225), 75, 0)
pygame.draw.circle(screen, (THECOLORS['red']), (675, 225), 75, 0)
pygame.draw.circle(screen, (THECOLORS['yellow']), (450, 375), 75, 0)
pygame.draw.circle(screen, (THECOLORS['green']), (600, 375), 75, 0)

pygame.draw.circle(screen, (THECOLORS['white']), (375, 225), 65, 0)
pygame.draw.circle(screen, (THECOLORS['white']), (525, 225), 65, 0)
pygame.draw.circle(screen, (THECOLORS['white']), (675, 225), 65, 0)
pygame.draw.circle(screen, (THECOLORS['white']), (450, 375), 65, 0)
pygame.draw.circle(screen, (THECOLORS['white']), (600, 375), 65, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
