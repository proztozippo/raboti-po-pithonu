xs, ys = map(int, input("введите x и y слона через пробел: ").split())
x1, y1 = map(int, input("введите x и y точки назначения слона через пробел: ").split())

# проверка нахождения на одной диагонали 2х точек
if (xs + ys == x1 + y1) or (xs - x1 == ys - y1):
    print("da")
else:
    print("net")