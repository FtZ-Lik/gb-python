gain = int(input("Выручка: "))
lose = int(input("Издержки: "))
if lose > gain:
    print("Убыток")
else:
    profit = (gain - lose)
    print(f"Прибыль {profit}")
    print(f"Рентабельность: {profit / gain}")
    employees = int(input("Количество сотрудников: "))
    print(f"Прибыль на 1 сотрудника: {profit / employees}")
