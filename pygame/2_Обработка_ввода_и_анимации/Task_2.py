import pygame
import sys


pygame.init()

screen = pygame.display.set_mode((640, 480))
rect = pygame.Rect(50, 50, 10, 10)
config = ['right'] * 10 + ['down'] * 9 + ['left'] * 9 + ['up'] * 9 + ['stop']

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for elem in config:
        if elem == 'left':
            rect.move_ip(-10, 0)
            pygame.time.delay(50)
        elif elem == 'right':
            rect.move_ip(10, 0)
            pygame.time.delay(50)
        elif elem == 'up':
            rect.move_ip(0, -10)
            pygame.time.delay(50)
        elif elem == 'down':
            rect.move_ip(0, 10)
            pygame.time.delay(50)
        elif elem == 'stop':
            pygame.time.delay(1000)
            pygame.quit()
            sys.exit()

        pygame.draw.rect(screen, (255, 0, 0), rect, 0)
        pygame.display.flip()


