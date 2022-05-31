# -*- coding: utf-8 -*-
"""
Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""

file1 = open("lesson5_task1_file.txt", 'w')
user_string = input("Введите строку: ")
while user_string != "":
    print(user_string, file = file1)
    user_string = input("Введите строку: ")
file1.close()
