def count_positive_numbers(a, b, c):
    count = 0
    if a > 0:
        count += 1
    if b > 0:
        count += 1
    if c > 0:
        count += 1
    return count

a = float(input("Введіть перше число (a): "))
b = float(input("Введіть друге число (b): "))
c = float(input("Введіть третє число (c): "))

positive_count = count_positive_numbers(a, b, c)

print("Кількість додатних чисел:", positive_count)
