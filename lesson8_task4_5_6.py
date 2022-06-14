# -*- coding: utf-8 -*-
"""
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием.
Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).

6. Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""
class Storage:
    _max_capacity = 500
    _current_capacity = 0
    _units = []
    _units_quantity = {"Printers":0, "Scaners":0, "Xeroxs":0}

    def add_unit(self, object_of_keeping):
        if self._current_capacity + 1 <= self._max_capacity:
            self._current_capacity += 1
            self._units.append(object_of_keeping)
            object_of_keeping.location = 'Склад'
            if isinstance(object_of_keeping, Printer):
                self._units_quantity['Printers'] += 1
            elif isinstance(object_of_keeping, Scaner):
                self._units_quantity['Scaners'] += 1
            elif isinstance(object_of_keeping, Xerox):
                self._units_quantity['Xeroxs'] += 1
            else:
                print(f"Неопознанный объект.")
        else:
            print(f"Превышение максимальной вместимости склада. Осталось {self._max_capacity - self._current_capacity} свободных мест.")

    def remove_unit(self, object_of_keeping, location):
        if object_of_keeping in self._units:
            self._current_capacity -= 1
            self._units.remove(object_of_keeping)
            object_of_keeping.location = location
            if isinstance(object_of_keeping, Printer):
                self._units_quantity['Printers'] -= 1
            elif isinstance(object_of_keeping, Scaner):
                self._units_quantity['Scaners'] -= 1
            elif isinstance(object_of_keeping, Xerox):
                self._units_quantity['Xeroxs'] -= 1
        else:
            print(f"Объект отсутствует на складе.")
    
    def info(self):
        print(f"Заполненность: {self._current_capacity} / {self._max_capacity}")
        print("На складе хранится следующее количество обьектов: " + str(self._units_quantity))


class OfficeEquipment:
    def __init__(self, name, inventory_number, location):
        self.name = name
        self.inventory_number = inventory_number
        self.location = location


class Printer(OfficeEquipment):
    def __init__(self, name, inventory_number, location, resource_of_pages):
        super().__init__(name, inventory_number, location)
        self.resource_of_pages = resource_of_pages


class Scaner(OfficeEquipment):
    def __init__(self, name, inventory_number, location, dpi):
        super().__init__(name, inventory_number, location)
        self.dpi = dpi


class Xerox(OfficeEquipment):
    def __init__(self, name, inventory_number, location, speed_of_copy):
        super().__init__(name, inventory_number, location)
        self.speed_of_copy = speed_of_copy


def test_of_work():
    test_obj = Printer('HP', '00001', 'отдел 1', 1000)
    storage = Storage()
    print("Создан тестовый обьект, его текущее положение: " + test_obj.location)
    storage.add_unit(test_obj)
    print("Тестовый обьект был перемещен на склад. Его текущее положение: " + test_obj.location)
    print("На складе хранится следующее количество обьектов: " + str(storage._units_quantity))
    storage.remove_unit(test_obj, "отдел 2")
    print("Тестовый обьект был перемещен со склада. Его текущее положение: " + test_obj.location)
    print("На складе хранится следующее количество обьектов: " + str(storage._units_quantity))
    del test_obj


def filling_database():
    answer = input("Добавить устройство в базу данных? (Y/N) или (Д/Н): ").upper()
    number = 1
    while answer not in ('N', 'Н'):
        if answer in ('Y', 'Д'):
            good_type = input('Тип устройства (P - принтер, S - сканер, X - ксерокс): ').upper()
            if good_type not in ('P', 'S', 'X'):
                print("Неверно указан тип устройства, попробуйте ещё раз.")
                continue
            good_name = input('Название устройства: ')
            good_inventory_number = input('Инвентарный номер устройства: ')
            good_location = input('Местоположение устройства: ')
            if good_type == 'P':
                good_resource_of_pages = input('Ресурс 1 картриджа (страниц): ')
                if good_resource_of_pages.isdigit():
                    good_resource_of_pages = int(good_resource_of_pages)
                    globals()['obj_' + str(number)] = Printer(good_name, good_inventory_number, good_location, good_resource_of_pages)
                else:
                    print("Неверно указан ресурс картриджа устройства, попробуйте ещё раз.")
                    continue
            elif good_type == 'S':
                good_dpi = input('Разрешение сканирования устройства (dpi): ')
                if good_dpi.isdigit():
                    good_dpi = int(good_dpi)
                    globals()['obj_' + str(number)] = Scaner(good_name, good_inventory_number, good_location, good_dpi)
                else:
                    print("Неверно указано разрешение сканирования устройства, попробуйте ещё раз.")
                    continue
            elif good_type == 'X':
                good_speed_of_copy = input('Скорость копирования (сек/шт.): ')
                if good_speed_of_copy.isdigit():
                    good_speed_of_copy = int(good_speed_of_copy)
                    globals()['obj_' + str(number)] = Xerox(good_name, good_inventory_number, good_location, good_speed_of_copy)
                else:
                    print("Неверно указан ресурс картриджа устройства, попробуйте ещё раз.")
                    continue
            print("Устройство успешно добавлено.")
            number += 1
        answer = input("Добавить устройство в базу данных? (Y/N) или (Д/Н): ").upper()


if input("Провести тестирование работы класса? (Y/N): ").upper() == 'Y':
    test_of_work()
filling_database()
