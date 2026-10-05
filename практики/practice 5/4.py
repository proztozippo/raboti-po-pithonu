import math
pi = 3.14

def calculate_rectangle_area(width, height): #для вычисления полощади пррямоугольника
    area_rect = width * height
    return area_rect

def calculate_circle_area(radius): #для вычисления площади круга
    area_circle = radius ** 2 * pi
    return area_circle

width, height = map(int, input("введите длину и ширину прямоугольника: ").split())#просим радиус круга и вычисл ее площадь
print(calculate_rectangle_area(width, height))

area_circle = int(input("введите радиус круга: "))#просим радиус круга и вычисл ее площадь
print(calculate_circle_area(area_circle))