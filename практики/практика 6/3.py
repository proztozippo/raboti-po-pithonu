x1, y1 = map(int, input("введите x1 и y1 через пробел: ").split())
x2, y2 = map(int, input("введите x2 и y2 через пробел: ").split())

w = "white"
r = "red"
cord_1 = 0
cord_2 = 0
if y1 % 2 == 0 and x1 % 2 == 0:
    cord_1 = w
elif y1 % 2 == 0 and x1 % 2 == 1:
    cord_1 = r
elif y1 % 2 == 1 and x1 % 2 == 1:
    cord_1 = w
elif y1 % 2 == 1 and x1 % 2 == 0:
    cord_1 = r


if y2 % 2 == 0 and x2 % 2 == 0:
    cord_2 = w
elif y2 % 2 == 0 and x2 % 2 == 1:
    cord_2 = r
elif y2 % 2 == 1 and x2 % 2 == 1:
    cord_2 = w
elif y2 % 2 == 1 and x2 % 2 == 0:
    cord_2 = r

if cord_1 == cord_2:
    print("цвета одинаковы")
else:
    print("цвета разные")