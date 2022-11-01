'''7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
'''


import json

file_output = open('Task_7.txt', 'r')
content = file_output.readlines()
file_output.close()

print(content)

list_content = []
for a in content:
    a = a.split()
    list_content.append(a)

print(list_content)

dict_profit = {}
av_profit = 0
av_profit_count = 0
for a in list_content:
    dict_profit[a[0]] = int(a[2]) - int(a[3])
    if int(a[2]) - int(a[3]) > 0:
        av_profit = av_profit + int(a[2]) - int(a[3])
        av_profit_count = av_profit_count + 1

dict_av_profit = {'average_profit': av_profit / av_profit_count}

list_fin = [dict_profit, dict_av_profit]
print(list_fin)

with open('Task_7.json', 'w') as f:
    json.dump(list_fin, f)


