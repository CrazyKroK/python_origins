import pygame
import sys

pygame.init()

window = pygame.display.set_mode((640, 480))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('Left')
            elif event.key == pygame.K_RIGHT:
                print('Right')
            elif event.key == pygame.K_UP:
                print('Up')
            elif event.key == pygame.K_DOWN:
                print('Down')

