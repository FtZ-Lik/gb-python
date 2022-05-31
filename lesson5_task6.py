# -*- coding: utf-8 -*-
"""
Сформировать (не программно) текстовый файл.
В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

f1 = open("lesson5_task6_file.txt", "r")
content = f1.read().split("\n")
for i in range(0, len(content)):
    content[i] = content[i].split()
    for j in range(1, 4):
        content[i][j] = content[i][j][:content[i][j].find("(")]
        if content[i][j].isdigit():
            content[i][j] = int(content[i][j])
        else:
            content[i][j] = 0
    content[i][1] = sum(content[i][j] for j in range(1, 4))
    content[i] = content[i][:2]
    content[i][0] = content[i][0][:-1]  #cut off simbol ":" at the end of subject name
content = dict(content)
print(content)
f1.close()
