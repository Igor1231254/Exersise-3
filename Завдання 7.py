def count_negative_numbers(a, b, c):
    count = 0
    if a < 0:
        count += 1
    if b < 0:
        count += 1
    if c < 0:
        count += 1
    return count

a = float(input("Введіть перше число (a): "))
b = float(input("Введіть друге число (b): "))
c = float(input("Введіть третє число (c): "))

negative_count = count_negative_numbers(a, b, c)

print("Кількість негативних чисел:", negative_count)
