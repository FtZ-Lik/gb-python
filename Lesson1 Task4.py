number = int(input("Input number: "))
max_digit = 0
while number != 0:
    a = number % 10
    if a > max_digit :
        max_digit = a
    number //= 10
print(max_digit)       
