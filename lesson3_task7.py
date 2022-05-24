# -*- coding: utf-8 -*-
"""
Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, но
каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().
"""

def int_func(input_string):
    return input_string[:1].upper() + input_string[1:]

print(" ".join(list(map(int_func, input("Введите строку из слов, через пробел: ").split()))))
