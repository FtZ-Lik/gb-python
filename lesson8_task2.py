# -*- coding: utf-8 -*-
"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class Div_Zero_Error(Exception):
    pass

number_1, number_2 = input("Введите делимое и делитель через пробел: ").split()

try:
    if number_2 == '0':
        raise Div_Zero_Error()  
    result = int(number_1) / int(number_2)
except ValueError:
    print("Вы ввели не число")
except Div_Zero_Error:
    print("Попытка деления на ноль")
else:
    print(result)
