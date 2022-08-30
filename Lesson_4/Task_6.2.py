'''Реализовать два небольших скрипта:
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее'''

from sys import argv
from itertools import cycle
my_list = argv[1:]
c = 0
for i in cycle(my_list):
    print(i, end=' ')
    c = c + 1
    if c > 10:
        break

# python Lesson_4\Task_6.2.py
