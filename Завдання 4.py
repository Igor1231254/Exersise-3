def process_numbers(x, y):
    if x < y:
        smaller = x
        larger = y
    else:
        smaller = y
        larger = x

    smaller_new = (x + y) / 2
    larger_new = 2 * x * y

    return (smaller_new, larger_new) if x < y else (larger_new, smaller_new)


x = float(input("Введіть перше число (x): "))
y = float(input("Введіть друге число (y): "))

if x == y:
    print("Числа не повинні бути рівні одне одному.")
else:

    result = process_numbers(x, y)

    print("Нове значення меншого числа:", result[0])
    print("Нове значення більшого числа:", result[1])
