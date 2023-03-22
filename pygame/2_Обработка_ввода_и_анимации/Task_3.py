import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((640, 480))
rect = pygame.Rect(40, 40, 20, 20)
color = (255, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and rect[0] > 0:
                rect.move_ip(-20, 0)
            elif event.key == pygame.K_RIGHT and rect[0] < 620:
                rect.move_ip(20, 0)
            elif event.key == pygame.K_UP and rect[1] > 0:
                rect.move_ip(0, -20)
            elif event.key == pygame.K_DOWN and rect[1] < 460:
                rect.move_ip(0, 20)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, rect, 0)
    pygame.display.flip()
