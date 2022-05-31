# -*- coding: utf-8 -*-
"""
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
"""

file1 = open("lesson5_task2_file.txt", 'r')
content = file1.readlines()
strings_quantity = len(content)
print(f"В файле {strings_quantity} строк, которые содержат следующее количество слов:")
for i in range(0, strings_quantity):
    content[i] = content[i].split()
    print(f"{i+1} - {len(content[i])}")
file1.close()
