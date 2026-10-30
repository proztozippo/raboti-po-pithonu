num = int(input("введите число остановы: "))
a = 1  # Начальная точка отсчёта

while a <= num:
    if not(5 <= a <= 9 or 17 <= a <= 37 or 78 <= a <= 87):
        print(a)
    a += 1
