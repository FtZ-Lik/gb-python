# -*- coding: utf-8 -*-
"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""

with open("lesson5_task5_file.txt", "w+") as file1:
    file1.write("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15")
    file1.seek(0)
    content = file1.readline().split()
content = list(map(int, content))
print(f"Сумма чисел в файле: {sum(content)}")
