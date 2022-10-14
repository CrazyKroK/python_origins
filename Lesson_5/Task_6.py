'''Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:

Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}'''


def multiple_replace(target_str, replace_values):
    for i, j in replace_values.items():
        target_str = target_str.replace(i, j)
    return target_str


dict_replacer = {"(л)": "", "(пр)": "", "(лаб)": "", ":": "", "—": ""}

file_output = open('Task_6.txt', 'r', encoding='utf-8')
content = file_output.readlines()
file_output.close()

list_content = []
for a in content:
    a = a.split()
    list_content.append(a)

clean_content = []
for b in list_content:
    pre_clean_content = []
    for c in b:
        c = multiple_replace(c, dict_replacer)
        pre_clean_content.append(c)
    clean_content.append(pre_clean_content)

subjects = []
hours = []
for d in clean_content:
    subjects.append(d.pop(0))
    my_sum = 0
    for h in d:
        try:
            h = int(h)
        except ValueError:
            h = 0
        my_sum = my_sum + h
    hours.append(my_sum)

my_dict = dict(zip(subjects, hours))

print(my_dict)
