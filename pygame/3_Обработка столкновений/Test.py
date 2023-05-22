# import sys
# import pygame
#
# pygame.init()
#
# WIDTH = 640
# HEIGHT = 480
#
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
#
# color = (172, 127, 127)
# cannon_shape = [(295, 460), (320, 410), (345, 460)]
# pygame.draw.polygon(screen, color, cannon_shape, 0)
#
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.flip()


# my_list = []
# n = 0
# while True:
#     cell = 'cell_' + str(n)
#     n = n + 1
#     my_list.append(cell)
#     print(my_list)

coord_dict = {1: [10, 10],
                   2: [120, 10],
                   3: [230, 10],
                   4: [340, 10],
                   5: [10, 120],
                   6: [120, 120],
                   7: [230, 120],
                   8: [340, 120],
                   9: [10, 230],
                   10: [120, 230],
                   11: [230, 230],
                   12: [340, 230],
                   13: [10, 340],
                   14: [120, 340],
                   15: [230, 340],
                   16: [340, 340]}

for value in coord_dict:
    coord_dict[value] = 0

print(coord_dict)

