# ввод х и у
x1, y1 = map(float, input("Введите x1, y1 точки A: ").split())
x2, y2 = map(float, input("Введите x2, y2 точки B: ").split())
x3, y3 = map(float, input("Введите x3, y3 точки C: ").split())


def evclid_distance(x1, y1, x2, y2):  # вычисление евклидова расстояния
    rast = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return rast

# расстояние между точками
a = evclid_distance(x1, y1, x2, y2)
b = evclid_distance(x2, y2, x3, y3)
c = evclid_distance(x3, y3, x1, y1)
p = (a + b + c)

# вычисление площади треугольника
s_triangle = ((p * (p - a) * (p - b) * (p - c)) ** 0.5)

print(f"площадь треугольника равна {s_triangle}")
