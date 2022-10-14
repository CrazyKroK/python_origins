'''Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.'''


def multiple_replace(target_str, replace_values):
    for i, j in replace_values.items():
        target_str = target_str.replace(i, j)
    return target_str


my_input_f = open("Task_4_input.txt", "r", encoding="utf-8")
content = my_input_f.readlines()
print(content)
my_input_f.close()

dict_replacer = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

my_output_f = open("Task_4_output.txt", "w", encoding="utf-8")
new_content = []
for elem in content:
    new_elem = multiple_replace(elem, dict_replacer)
    print(new_elem)
    new_content.append(new_elem)

my_output_f.writelines(new_content)
my_output_f.close()
