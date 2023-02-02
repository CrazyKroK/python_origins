"""Урок 8. ООП. Полезные дополнения

== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html"""

import random


def keg_ending(keg_count):
    if keg_count % 10 > 4 or keg_count % 10 == 0:
        return ' бочонков'
    elif keg_count % 10 == 1:
        return ' бочонок'
    else:
        return ' бочонка'


def is_number(i):
    """Проверка на число. Является ли элемент числом?"""
    try:
        float(i)
        return True
    except ValueError:
        return False


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def multiple_replace(target_str, replace_values):
    for i, j in replace_values.items():
        target_str = target_str.replace(i, j)
    return target_str


dict_replacer = {"[": "", "]": "", ",": "", "'": "", "(": "", ")": ""}


class LotoCard:
    def __init__(self, name):
        self.name = name
        """Создается список чисел. Они отсортированы в рамках каждой пятерки. Проверена уникальность каждой пятерки."""
        numbers = []
        while len(numbers) < 15:
            new_numbers = sorted(random.sample(range(1, 91), 5))
            if set(new_numbers) - set(numbers) == set(new_numbers):
                for elem in new_numbers:
                    numbers.append(elem)

        """Создается список позиций чисел"""
        number_pos = sorted(random.sample(range(1, 10), 5) +
                            random.sample(range(10, 19), 5) +
                            random.sample(range(19, 28), 5))

        """Создается словарь, состоящий из позиций чисел и самих чисел (основа для карточки)"""
        self.card = dict(zip(number_pos, numbers))

    def __str__(self):

        """Добавляет в словарь 'пустые' значение по ключам, которые не были созданы в __init__"""
        card_str = self.card
        new_key = 1
        while new_key < 28:
            if card_str.get(new_key) is None:
                card_str[new_key] = '  '
            new_key = new_key + 1

        """Добавляет пробел перед однозначными числами (1-9)."""
        new_card_str = dict()
        for i in card_str:
            if is_number(card_str[i]) is False:
                new_card_str[i] = card_str[i]
            else:
                if int(card_str[i]) < 10:
                    new_card_str[i] = '', card_str[i]
                else:
                    new_card_str[i] = card_str[i]

        """Добавление пунктира, убирание технических символов, разделение на 3 строки."""
        if len(self.name) % 2 > 0:
            self.name = self.name + '-'
        else:
            self.name = self.name
        read_card_str = '\n' + \
                        '-' * int((26 - len(self.name)) / 2) + self.name + \
                        '-' * int((26 - len(self.name)) / 2) + '\n' + \
                        str(list(dict(sorted(new_card_str.items())[0:9]).values())) + '\n' + \
                        str(list(dict(sorted(new_card_str.items())[9:18]).values())) + '\n' + \
                        str(list(dict(sorted(new_card_str.items())[18:]).values())) + '\n' + \
                        '-' * 26

        return multiple_replace(read_card_str, dict_replacer)

    def game(self, other):

        kegs = random.sample(range(1, 91), 90)
        for keg in kegs:
            if keg == kegs[0]:
                print('Номер вашего бочонка:', keg)
            else:
                print('Номер вашего следующего бочонка:', keg)
            print(self)
            print(other)
            answer = input('Есть ли номер этого бочонка в вашей карточке? (Y/N): ')
            while answer != 'Y' and answer != 'y' and answer != 'N' and answer != 'n':
                answer = input('Не понял вас. Введите свой ответ еще раз. (Y/N): ')
            else:
                if keg in self.card.values():
                    if answer == 'Y' or answer == 'y':
                        self.card.update({get_key(self.card, keg): '--'})
                        if set(self.card.values()) - set(range(1, 91)) == set(self.card.values()):
                            print('ВЫ ПОБЕДИЛИ! ВЫ ВЫЧЕРНУЛИ ВСЕ ЧИСЛА НА СВОЕЙ КАРТОЧКЕ!')
                            break
                        else:
                            print('\n' * 10, 'Верно! Вычеркиваем! Осталось ', 89 - kegs.index(keg),
                                  keg_ending(89 - kegs.index(keg)), sep='')
                    else:
                        print('Неверно! Вы проиграли!')
                        break
                else:
                    if answer == 'N' or answer == 'n':
                        print('\n' * 10, 'Верно! Осталось ', 89 - kegs.index(keg), keg_ending(89 - kegs.index(keg)),
                              sep='')
                    else:
                        print('Неверно! Вы проиграли!')
                        break
            if keg in other.card.values():
                other.card.update({get_key(other.card, keg): '--'})
            if set(other.card.values()) - set(range(1, 91)) == set(other.card.values()):
                print('Но, к сожалению, вы проиграли! Компьютер вычеркнул все числа раньше вас!')
                break


loto_card = LotoCard('Ваша карточка')
loto_card_2 = LotoCard('Карточка компьютера')
loto_card.game(loto_card_2)
