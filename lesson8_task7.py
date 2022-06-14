# -*- coding: utf-8 -*-
"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __str__(self):
        if self.real_part == 0:
            return f"{self.imaginary_part}i"
        if self.imaginary_part < 0:
            return f"{self.real_part} - {-self.imaginary_part}i"
        return f"{self.real_part} + {self.imaginary_part}i"

    def __add__(self, other):
        if type(other) == int:
            return ComplexNumber(self.real_part + other, self.imaginary_part)
        else:
            return ComplexNumber(self.real_part + other.real_part, self.imaginary_part + other.imaginary_part)

    def __sub__(self, other):
        if type(other) == int:
            return ComplexNumber(self.real_part - other, self.imaginary_part)
        else:
            return ComplexNumber(self.real_part - other.real_part, self.imaginary_part - other.imaginary_part)

    def __mul__(self, other):
        if type(other) == int:
            return ComplexNumber(self.real_part * other, self.imaginary_part * other)
        else:
            new_real = (self.real_part * other.real_part) - (self.imaginary_part * other.imaginary_part)
            new_imaginary = (self.real_part * other.imaginary_part) + (self.imaginary_part * other.real_part)
            return ComplexNumber(new_real, new_imaginary)


a = ComplexNumber(1, 1)
b = ComplexNumber(2, -2)
c = ComplexNumber(0, 3)
d = ComplexNumber(0, -4)
print(a, b, c, d, sep = ", ")
print(a + b)
print(c - d)
print(a * b)
print(a * c)
