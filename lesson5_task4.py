# -*- coding: utf-8 -*-
"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

num_dict = {"One":"Один", "Two":"Два", "Three":"Три", "Four":"Четыре"}
file1 = open("lesson5_task4_file1.txt", "r")
file2 = open("lesson5_task4_file2.txt", "w")
content = file1.read().split("\n")
for i in range(0, len(content)):
    content[i] = content[i].split(" — ")
    if content[i][0] in num_dict.keys():
        content[i][0] = num_dict[content[i][0]]
for pair in content:
    print(" — ".join(pair), file = file2)
file1.close()
file2.close()
