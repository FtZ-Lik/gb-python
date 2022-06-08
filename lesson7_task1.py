# -*- coding: utf-8 -*-
"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""
from copy import deepcopy
class Matrix():
    '''Класс Матрица в понятии Линейной Алгебры. Для класса реализованна только операция "сложение матриц"'''
    def __init__(self, list_of_lists):
        self._matrix = list_of_lists

    def __str__(self):
        result = str()
        for row in self._matrix:
            for element in row:
                result = result + str(element) + "\t"
            result = result + "\n"
        return result

    def __add__(self, other):
        if len(self._matrix) != len(other._matrix) or len(self._matrix[0]) != len(other._matrix[0]):
            print("Ошибка!!!\nРазные размеры матриц!")
            return None
        result = deepcopy(self._matrix)
        for i in range(len(self._matrix)):
            for j in range(len(self._matrix[i])):
                result[i][j] = self._matrix[i][j] + other._matrix[i][j]
        return Matrix(result)

if __name__ == "__main__":
    A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(A)
    B = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    C = A + B
    print(C)
    print(A + B)
