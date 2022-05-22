
my_list = input("Введите список через пробел: ").split()
for i in range(len(my_list)//2):
    my_list[i * 2], my_list[i * 2 + 1] = my_list[i * 2 + 1], my_list[i * 2]
print(my_list)
