# -*- coding: utf-8 -*-
"""
Реализуйте базовый класс Car.

    у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
    А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
    опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
    добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
    для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
"""
class Car:
    is_police = False
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
    def go(self):
        print(f"Машина {self.name} поехала!")
    def stop(self):
        print(f"Машина {self.name} остановилась!")
    def turn(self):
        print(f"Машина {self.name} повернула {input('Куда повернуть? (направо/налево/назад): ')}!")
    def show_speed(self):
        print("Скорость:", self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Скорость машины",self.name, ":", self.speed, "Превышение скорости!!!")
        else:
            print("Скорость машины",self.name, ":", self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Скорость машины",self.name, ":", self.speed, "Превышение скорости!!!")
        else:
            print("Скорость машины",self.name, ":", self.speed)


class PoliceCar(Car):
    is_police = True


car_1 = TownCar(65, "Белый", "BMW")
car_2 = SportCar(85, "Красный", "Ferrari")
car_3 = WorkCar(35, "Трактор", "Беларусь")
car_4 = PoliceCar(65, "Бело-Синий", "ДПС")
print("Доступ к атрибуту - Скорость 1 машины", car_1.speed)
car_1.go()
car_2.stop()
car_3.turn()
car_1.show_speed()
car_2.show_speed()
car_3.show_speed()
car_4.show_speed()
