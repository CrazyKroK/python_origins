'''Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного'''

from sys import argv
from itertools import count
start_gen = int(argv[1])
for i in count(start=start_gen, step=1):
    print(i, end=' ')
    if i > 16:
        print()
        break

# python Lesson_4\Task_6.1.py start_gen

