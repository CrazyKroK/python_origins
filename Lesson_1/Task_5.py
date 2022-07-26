# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
revenue = input('Введите значение выручки в рублях: ')
costs = input('Введите значение издержек в рублях: ')
revenue = float(revenue)
costs = float(costs)
if revenue > costs:
    profit = revenue - costs
    profitability = profit / revenue * 100
    print(f'Ваша прибыль составила {profit} руб.')
    print(f'Ваша рентабельность составила {profitability}%.')
    workers = input('Введите количество сотрудников в фирме: ')
    workers = int(workers)
    profit_on_worker = profit / workers
    print(f'Прибыль фирмы в расчете на одного сотрудника составила: {profit_on_worker} руб.')
elif revenue < costs:
    loss = costs - revenue
    print(f'Ваш убыток составил {loss} руб.')
else:
    print('Вы вышли в ноль.')
