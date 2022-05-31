# -*- coding: utf-8 -*-
"""
Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

file1 = open("lesson5_task3_file.txt", "r")
content = file1.readlines()
for i in range(0, len(content)):
    content[i] = content[i].split()
    content[i][1] = float(content[i][1])
content = dict(content)
list_of_low_salary = []
for name, salary in content.items():
    if salary < 20000:
        list_of_low_salary.append(name)
average_salary = sum(list(content.values())) / len(list(content.values()))
print("Оклад ниже 20000 у сотрудников: " + " ".join(list_of_low_salary))
print(f"Средний оклад: {average_salary}")
file1.close()
