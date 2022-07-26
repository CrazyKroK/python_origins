''' Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами. '''

from My_hw_module import salary_calc
from sys import argv

my_wage_rate = float(argv[1])
my_hours = float(argv[2])
my_bonus = float(argv[3])
print('Ваша заработная плата составит:', salary_calc(my_wage_rate, my_hours, my_bonus))


