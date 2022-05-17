a, b = int(input("a = ")), int(input("b = "))
i = 1
print(f"{i}-й день: {a}")
while a < b:
    i += 1
    a *= 1.1
    print(f"{i}-й день: {a:.2f}")
print(f"Ответ: {i}-й день")
