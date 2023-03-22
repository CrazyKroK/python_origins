import pygame
import sys
from pygame.color import THECOLORS

pygame.init()

screen = pygame.display.set_mode((1200, 800))
screen.fill(THECOLORS['cadetblue1'])

grass = pygame.Rect(0, 600, 1200, 200)
house = pygame.Rect(400, 400, 400, 200)
chimney = pygame.Rect(400, 200, 50, 100)
pygame.draw.rect(screen, (THECOLORS['chartreuse3']), grass, 0)
pygame.draw.rect(screen, (THECOLORS['grey']), chimney, 0)
pygame.draw.rect(screen, (THECOLORS['black']), chimney, 1)
pygame.draw.rect(screen, (THECOLORS['burlywood4']), house, 0)
pygame.draw.polygon(screen, (THECOLORS['firebrick4']), [(300, 400), (600, 100), (900, 400)], 0)
pygame.draw.rect(screen, (THECOLORS['black']), house, 1)
pygame.draw.polygon(screen, (THECOLORS['black']), [(300, 400), (600, 100), (900, 400)], 1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
