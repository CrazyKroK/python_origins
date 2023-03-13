# a = [1, 2, 3]
# a = set(a)
# b = {3, 4, 5}
# if a - b == a:
#     print('!')
# a = input()
# if a != 'a' and a != 'b':
#     print('УРА')
# import time
# timing = time.time()
# while True:
#     if time.time() - timing > 3.0:
#         print('Вы проиграли!')
#         break
a = {1, 2, 3, 4}
b = 5
if b not in a:
    print('Ура')
