''' Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.'''


def multiple_replace(target_str, replace_values):
    for i, j in replace_values.items():
        target_str = target_str.replace(i, j)
    return target_str


dict_replacer = {"'": "", "] [": "\n", "[": "", "]": "", ",": ""}


class Matrix:
    def __init__(self, matrix=None):
        if matrix is None:
            self.quantity_str = int(input('Введите количество строк в матрице: '))
            self.len_str = int(input('Введите количество столбцов в матрице: '))
            cycle = 0
            cycle_str = 1
            self.matrix = []
            while cycle < self.quantity_str:
                new_str = input('Введите элементы ' + str(cycle_str) + '-й строки через пробел: ').split()
                quantity_elem = len(new_str)
                if quantity_elem != self.len_str:
                    print('Вы ввели неверное количество элементов строки!')
                else:
                    self.matrix.append(new_str)
                    cycle = cycle + 1
                    cycle_str = cycle_str + 1
        else:
            self.matrix = matrix

    def __str__(self):
        matrix_str = multiple_replace(' '.join(str(e) for e in self.matrix), dict_replacer)
        return matrix_str

    def __add__(self, other):
        if self.quantity_str is other.quantity_str and self.len_str is other.len_str:
            cycle = 0
            matrix_sum = []
            while cycle < self.quantity_str:
                matrix_sum.append([int(x) + int(y) for x, y in zip(self.matrix[cycle], other.matrix[cycle])])
                cycle = cycle + 1
            return Matrix(matrix_sum)
        else:
            print('Вы пытаетесь сложить разноразмерные матрицы!')


matrix_1 = Matrix()
matrix_2 = Matrix()
print(matrix_1 + matrix_2)
