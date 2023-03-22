# https://python-course.readthedocs.io/projects/elementary/en/latest/lessons/19-animations.html

import pygame
import sys

animation_set = [pygame.image.load(f"icons/frame{i}.png") for i in range(1, 3)]

window = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()
i = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((0, 0, 0))
    window.blit(animation_set[i // 30], (100, 20))
    i += 1
    if i == 60:
        i = 0

    pygame.display.flip()
    clock.tick(60)
