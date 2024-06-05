def find_divisors(a, b, c, k):
    divisors = []
    if a % k == 0:
        divisors.append('a')
    if b % k == 0:
        divisors.append('b')
    if c % k == 0:
        divisors.append('c')
    return divisors

a = int(input("Введіть перше число (a): "))
b = int(input("Введіть друге число (b): "))
c = int(input("Введіть третє число (c): "))
k = int(input("Введіть число (k): "))

divisors = find_divisors(a, b, c, k)

if divisors:
    print(f"Число {k} є дільником чисел: {', '.join(divisors)}.")
else:
    print(f"Число {k} не є дільником жодного з чисел a, b, c.")
