temp = float(input("введите свою температуру(в градусах цельсия): "))
pressure = int(input("введите свое давление(верхнее): "))
pulse = int(input("введите свой пульс: "))

if 36 < temp < 37 and 110 <= pressure <= 130 and 60 <= pulse <= 100:
    print("нормальное состояние")
elif (35 < temp < 36 or 37 < temp < 38) and (105 <= pressure <= 110 or 130 <= pressure <= 140) and (55 <= pulse <= 60 or 100 <= pulse <= 110):
    print("у вас легкое недомогание")
elif (35 > temp or temp > 38) and (pressure < 105 or pressure > 110) and (pulse < 55 or pulse > 110):
    print("требуется врач")