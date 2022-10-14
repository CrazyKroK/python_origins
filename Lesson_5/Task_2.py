'''Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.'''

my_f = open("Task_2.txt", "r")
content = my_f.readlines()
lines = len(content)
words = 0
for elem in content:
    words = words + elem.count(' ') + 1

# print(content)
print('Строк в документе:', lines)
print('Слов в документе:', words)

my_f.close()
