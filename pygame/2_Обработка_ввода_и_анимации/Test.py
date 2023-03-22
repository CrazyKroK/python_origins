import pygame
import sys

# pygame.init()
#
# screen = pygame.display.set_mode((1200, 800))
#
# for event in pygame.event.get():
#     print(event, end='\n')
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()

pygame.init()

screen = pygame.display.set_mode((640, 480))
x = 40
y = 40
rect = pygame.Rect(x, y, 120, 120)
color = (255, 255, 255)

pygame.draw.rect(screen, color, rect, 0)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            rect = pygame.Rect(x, y, 120, 120)
            color = (0, 0, 0)
            pygame.draw.rect(screen, color, rect, 0)
            pygame.display.flip()

            x = x + 120
            rect = pygame.Rect(x, y, 120, 120)
            color = (255, 255, 255)
            pygame.draw.rect(screen, color, rect, 0)
            pygame.display.flip()





