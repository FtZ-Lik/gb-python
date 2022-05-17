'''1. Поработайте с переменными, создайте несколько, выведите на экран. Запросите у
пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.'''

var_1 = 42
var_2 = 'Hello, world'
print(var_1, var_2, sep='\n')
var_1 = int(input("Input number: "))
print(var_1)
var_2 = input("Input string: ")
print("Your string is - " + var_2)