# -*- coding: utf-8 -*-
"""
Реализовать базовый класс Worker (работник).

    определить атрибуты: name, surname, position (должность), income (доход);
    последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
    создать класс Position (должность) на базе класса Worker;
    в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
    проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

"""
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self._income = {"wage": float(wage), "bonus": float(bonus)}
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def get_total_income(self):
        return sum(self._income.values())
    def get_full_name(self):
        return f"{self.name} {self.surname}"


w1_input = input("Имя Фамилия Должность Оклад Премия: ").split()
worker_1 = Position(*w1_input)
w2_input = input("Имя Фамилия Должность Оклад Премия: ").split()
worker_2 = Position(*w2_input)
print(worker_1.get_full_name(), worker_1.get_total_income())
print(worker_2.get_full_name(), worker_2.get_total_income())
