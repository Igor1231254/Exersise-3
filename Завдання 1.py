def process_numbers(a, b, c):

    numbers = [a, b, c]

    for i in range(len(numbers)):
        if numbers[i] >= 0:
            numbers[i] = numbers[i] ** 2
        else:
            numbers[i] = numbers[i] ** 4

    return numbers

a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))

result = process_numbers(a, b, c)

print("Результат обробки чисел:", result)
