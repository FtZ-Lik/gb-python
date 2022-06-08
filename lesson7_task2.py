# -*- coding: utf-8 -*-
"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod
class Clothes(ABC):
    '''Обобщенный класс Одежда'''
    count_fabric = 0

    @property
    @abstractmethod
    def fabric(self):
        pass

class Coat(Clothes):
    '''Класс Пальто'''
    def __init__(self, V):
        self._size = float(V)
        Clothes.count_fabric += self.fabric

    @property
    def fabric(self):
        return self._size/6.5 + 0.5

class Suit(Clothes):
    '''Класс Костюм'''
    def __init__(self, H):
        self._hight = float(H)
        Clothes.count_fabric += self.fabric

    @property
    def fabric(self):
        return 2 * self._hight + 0.3


coat_1 = Coat(6.5)
print(coat_1.fabric)
suit_1 = Suit(3)
print(suit_1.fabric)
print(Clothes.count_fabric)
