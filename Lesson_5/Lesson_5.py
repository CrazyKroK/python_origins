# file = open('test.txt')
# lines = file.readlines()
# print(lines)
# for line in lines:
#     print(line.strip())

# print(file.readline(), end='')
# print(file.readline(), end='')
# print(file.readline(), end='')

'''
Режим 	Описание
r	    Открыть файл на чтение (режим по умолчанию)
w	    Открыть на запись. При этом удалить содержимое файла. Если файла нет, создать новый.
x	    Открыть файл на запись, если его нет. Если файл есть, он не будет создан.
a	    Открыть файл на дозапись. Добавить информацию в конец файла.
b	    Открыть файл в двоичном формате.
t	    Открыть файл в текстовом формате (режим по умолчанию)
+	    Открыть файл на чтение и запись
Всего в режиме может быть 3 символа:
r, w, x, a - опции для первого символа,
a, b - опции для второго символа
+ - опция для третьего символа
'''

# file = open('test.txt', 'w')  # режим доступа к файлу
# file.write('Kirill')

# file = open('test.txt', 'a')  # режим доступа к файлу
# qwe = ['1', '2', '3']
# file.writelines(qwe)
# file.write('\n'.join(qwe))
# file.close()

# file = open('test.txt')
# print(file.name)
# print(file.closed)
# print(file.mode)

# Менеджер контекста закрвает файл сразу после выхода из него чтобы не забывать закрывать
# with open('test.txt') as f:
#     print(f)
#     print(f.closed)
#
# print(f.closed)

# МЕТОДЫ TELL И SEEK

# with open('test.txt', 'w+') as f:
#     f.write('111\n')
#     f.write('222\n')
#     f.write('333')
#     print(f.tell())
#     print(f.read())  # в этом случае он напечатает пустоту,т.к. указатель стоит в конце файла.

# with open('test.txt', 'w+') as f:
#     f.write('111\n')
#     f.write('222\n')
#     f.write('333')
#     print(f.tell())  # определет позцию указателя в байтах (не в символах)
#     if f.tell() != 0:
#         f.seek(0)  # Передвигает указатель на нужную позицию в байтах (не в символах)
#     print(f.tell())
#     print(f.read())

# with open('Test.txt', 'w') as f:
#     print('QWE', file=f)

# JSON используется для сохранения значений переменных

# import json
# data = {'income': {'salary': 50000, 'bonus': 10000}}
# with open('test2.json', 'w') as f:
#     json.dump(data, f)

# with open('test2.json') as f:
#     data = json.load(f)
# print(data)
# print(type(data))

# loads и dumps используется для просмотра внешнего вида данных просле загрузки/сохранения

# SHUTIL

# import shutil
# shutil.copyfile('test.txt', '1/test.txt')  # копирует с метаданными
# shutil.copy('test.txt', '1/test.txt')  # копирует без метаданных
# shutil.rmtree('1')  # удаляет папку
# shutil.move('что', 'куда')

# import os
# qwe = r"C:\Users\Gabe_Newell\anaconda3\lib\shutil.py"  # r вначале пути дает возможность воспринимать
# путь как а строку
# без спецсимволов типа \n и т.д.
# print(os.path.basename(qwe))  # выдает конечное название файла
# print(os.path.splitext(qwe))  # дает кортеж, отсекает расширение файла
# os.path.join()  # собирает путь из нескольких значений, сам расставляет слэши

