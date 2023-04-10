import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640, 480))
start = [pygame.image.load("icons/Task_5/0.png")]
move_left = [pygame.image.load(f"icons/Task_5/l{i}.png") for i in range(3, 6)]
move_right = [pygame.image.load(f"icons/Task_5/r{i}.png") for i in range(3, 6)]

sprite_loc = [320, 60]
num = 0
num_l = 0
num_r = 0
animation_set = start

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        screen.blit(animation_set[num], sprite_loc)
        pygame.display.flip()

        if event.type == pygame.KEYDOWN:
            screen.fill((0, 0, 0))
            if event.key == pygame.K_LEFT and sprite_loc[0] > 0:
                animation_set = move_left
                num = num_l
                sprite_loc[0] = sprite_loc[0] - 10
                num_l = num_l + 1
            elif event.key == pygame.K_RIGHT and sprite_loc[0] < 620:
                animation_set = move_right
                num = num_r
                sprite_loc[0] = sprite_loc[0] + 10
                num_r = num_r + 1

        if num_r > 2:
            num_r = 0

        if num_l > 2:
            num_l = 0


