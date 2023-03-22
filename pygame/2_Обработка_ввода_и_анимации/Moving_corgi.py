# https://python-course.readthedocs.io/projects/elementary/en/latest/lessons/19-animations.html
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640, 480))
sprite = pygame.image.load("icons/icons8-corgi-48.png")

sprite_loc = [20, 20]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        screen.blit(sprite, sprite_loc)
        pygame.display.flip()

        if event.type == pygame.KEYDOWN:
            screen.fill((0, 0, 0))
            if event.key == pygame.K_LEFT:
                sprite_loc[0] = sprite_loc[0] - 20
            elif event.key == pygame.K_RIGHT:
                sprite_loc[0] = sprite_loc[0] + 20
            elif event.key == pygame.K_UP:
                sprite_loc[1] = sprite_loc[1] - 20
            elif event.key == pygame.K_DOWN:
                sprite_loc[1] = sprite_loc[1] + 20

            screen.blit(sprite, sprite_loc)
            pygame.display.flip()
