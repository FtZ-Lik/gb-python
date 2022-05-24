# -*- coding: utf-8 -*-
"""
Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
"""

def int_func(string):
    return string[:1].upper() + string[1:]

print(int_func(input("Введите слово с маленькой буквы: ")))
