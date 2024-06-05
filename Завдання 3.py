def triangle_properties(angle1, angle2):

    if angle1 <= 0 or angle2 <= 0 or angle1 + angle2 >= 180:
        return "Трикутник не існує."


    angle3 = 180 - (angle1 + angle2)

    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        return "Трикутник існує і є прямокутним."
    else:
        return "Трикутник існує, але не є прямокутним."


angle1 = float(input("Введіть величину першого кута (в градусах): "))
angle2 = float(input("Введіть величину другого кута (в градусах): "))

result = triangle_properties(angle1, angle2)

print(result)
