"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
класса (метод init()), который должен принимать данные (список списков)
для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц). Результатом сложения
должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый
элемент первой строки первой матрицы складываем с первым элементом
первой строки второй матрицы и т.д.
"""

cols = 3
rows = 3
n = 3


class Matrix:
    def __init__(self):
        self.mtx = [[0 for i in range(cols)] for j in range(rows)]

    def input_matrix(self, x):
        for i in range(cols):
            for j in range(rows):
                self.mtx[i][j] = x[i][j]

    def __str__(self):
        for row in self.mtx:
            for i in row:
                print(f"{i:4}", end=' ')
            print()
        return ''

    def __add__(self, x):
        result = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(cols):
            for j in range(rows):
             result[i][j] = self.mtx[i][j] + x.mtx[i][j]

        for i in range(cols):
            for j in range(rows):
                print(result[i][j], end=' ')
            print()


mtx1 = Matrix()
mtx2 = Matrix()

a = [[13, 7, 4],
      [12, 6, 3],
      [11, 5, 2]]

b = [[1, 1, 1],
      [2, 2, 2],
      [3, 3, 3]]

mtx1.input_matrix(a)
mtx2.input_matrix(b)
mtx1.__str__()
print()
mtx2.__str__()

print("Сумма матриц : ")
mtx1 + mtx2


# result = [[A[i][j] + B[i][j] for j in range
# (len(A[0]))] for i in range(len(A))]
#
# for r in result:
#     print(r)


