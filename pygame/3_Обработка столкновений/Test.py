import random
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

# coord_dict = {1: [10, 10],
#                    2: [120, 10],
#                    3: [230, 10],
#                    4: [340, 10],
#                    5: [10, 120],
#                    6: [120, 120],
#                    7: [230, 120],
#                    8: [340, 120],
#                    9: [10, 230],
#                    10: [120, 230],
#                    11: [230, 230],
#                    12: [340, 230],
#                    13: [10, 340],
#                    14: [120, 340],
#                    15: [230, 340],
#                    16: [340, 340]}
#
# for value in coord_dict:
#     coord_dict[value] = 0
#
# print(coord_dict)

# cell_pos_dict = {1.1: None,
#                  1.2: None,
#                  1.3: None,
#                  1.4: None,
#                  2.1: None,
#                  2.2: None,
#                  2.3: None,
#                  2.4: None,
#                  3.1: None,
#                  3.2: None,
#                  3.3: None,
#                  3.4: None,
#                  4.1: None,
#                  4.2: None,
#                  4.3: None,
#                  4.4: None}
#
# for key in cell_pos_dict.keys():
#     coord_1 = (round(key % 1, 1) * 1100) - 100
#     coord_2 = (key // 1 * 110) - 100
#     coord = [coord_1, coord_2]
#     print(coord)
#
# sequence = [1.1, 1.2, 1.3, 1.4, 2.2, 2.2, 2.3, 2.4, 3.1, 3.2, 3.3, 3.4, 4.1, 4.2, 4.3, 4.4]
# cell_pos_key_try = random.choice(sequence)
# print(cell_pos_key_try)
#
# print(type(list(cell_pos_dict.values())))

# a = {1: 4, 2: 5, 3: 6}
# res = list(a.items())
# b = dict(reversed(list(a.items())))
# print(b)

print(41 // 10)


