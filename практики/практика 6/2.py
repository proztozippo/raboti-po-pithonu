a = int(input("введите число на рулетке"))
if 0 > a > 36:
    print("ошибка ввода")
elif a == 0:
    print("зеленый")
elif 1 <= a <= 10 and a % 2 == 0: # от 1 до 10
    print("черный")
elif 1 <= a <= 10 and a % 2 != 0:
    print("красный")
else:
    if 11 <= a <= 18 and a % 2 == 0: # от 11 до 18
        print("красный")
    elif 11 <= a <= 18 and a % 2 != 0:
        print("черный")
    else:
        if 19 <= a <= 28 and a % 2 == 0: # от 19 до 28
            print("черный")
        elif 19 <= a <= 28 and a % 2 != 0:
            print("красный")
        else:
            if 29 <= a <= 36 and a % 2 == 0: # от 29 до 26
                print("красный")
            else:
                print("черный")

