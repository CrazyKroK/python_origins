import pygame
import sys
import time
import random
from pygame.color import THECOLORS

pygame.init()

screen = pygame.display.set_mode((1200, 800))
screen.fill(THECOLORS['white'])

font = pygame.font.SysFont('couriernew', 40)

text = 1
x = 0
y = 0

while x <= 1200 and y <= 800:
    r = pygame.Rect(x, y, 100, 100)
    pygame.draw.rect(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), r, 0)
    pygame.draw.rect(screen, (THECOLORS['white']), r, 3)

    lettering = font.render(str(text), True, THECOLORS['black'])
    screen.blit(lettering, (x + 5, y + 5))

    if x <= 1000:
        x = x + 100
    else:
        y = y + 100
        x = x - 1100
    text = text + 1
    pygame.display.update()
    time.sleep(0.05)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
