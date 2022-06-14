# -*- coding: utf-8 -*-
"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
class Date:
    date, day, month, year = [None] * 4
    def __init__(self, date):
        Date.date = date

    @classmethod
    def m_1(cls):
        cls.day, cls.month, cls.year = list(map(int, cls.date.split("-")))

    @staticmethod
    def m_2():
        if [Date.day, Date.month, Date.year] == [None] * 3:
            print('Сначала вызовите метод .m_1()')
        elif not(0 < Date.year < 2050):
            print('Недопустимое значение года')
        elif not(0 < Date.month < 13):
            print("Недопустимое значение месяца")
        else:
            if Date.month == 2:
                days_in_month = 29 if Date.year % 4 == 0 else 28
            else:
                days_in_month = 31 if Date.month in (1, 3, 5, 7, 8, 10, 12) else 30
            if not(0 < Date.day <= days_in_month):
                print("Недопустимое значение дня")
            else:
                print('Валидация успешно пройдена, все значения в допустимых диапазонах')


Date('11-11-2011')
Date.m_2()
Date('11-11-2011').m_1()
Date.m_2()
Date('13-13-2011').m_1()
Date.m_2()
Date('29-02-2011').m_1()
Date.m_2()
Date('29-02-2012').m_1()
Date.m_2()
