a = int(input("Введіть перше число (a): "))
b = int(input("Введіть друге число (b): "))

if a != b:

    max_value = max(a, b)
    a = max_value
    b = max_value
else:

    a = 0
    b = 0

print("Нове значення першого числа (a):", a)
print("Нове значення другого числа (b):", b)
