def point_location(x, y):
    if x == 0 and y == 0:
        return "Точка знаходиться в початку координат."
    elif x == 0:
        return "Точка знаходиться на осі Y."
    elif y == 0:
        return "Точка знаходиться на осі X."
    elif x > 0 and y > 0:
        return "Точка знаходиться в першому координатному куті."
    elif x < 0 and y > 0:
        return "Точка знаходиться в другому координатному куті."
    elif x < 0 and y < 0:
        return "Точка знаходиться в третьому координатному куті."
    elif x > 0 and y < 0:
        return "Точка знаходиться в четвертому координатному куті."


x = float(input("Введіть координату x точки A: "))
y = float(input("Введіть координату y точки A: "))


location = point_location(x, y)


print(location)
