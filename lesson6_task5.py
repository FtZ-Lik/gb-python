# -*- coding: utf-8 -*-
"""
Реализовать класс Stationery (канцелярская принадлежность).

    определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
    создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
    в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
    создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
class Stationery():
    title = "Канцелярская принадлежность"
    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркером")


item_1 = Stationery()
item_2 = Pen()
item_3 = Pencil()
item_4 = Handle()
item_1.draw()
item_2.draw()
item_3.draw()
item_4.draw()
