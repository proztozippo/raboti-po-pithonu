#В мире ведьмака существуют монеты с номиналами 1,5,10,25.
#Напишите программу, которая определяет,
#какое минимальное количество чеканных монет нужно заплатить ведьмаку.
num = int(input("введите цену ведьмака: "))

while num != 0:
    if num // 25 > 1:
        mon = 25
        co_new = num // mon
        num -= co_new * mon
    elif num // 10 > 1:
        mon = 10
        co_new = num // mon
        num -= co_new * mon
    elif num // 5 > 1:
        mon = 5
        co_new = num // mon
        num -= co_new * mon
    elif num // 1 > 1:
        mon = 1
        co_new = num // mon
        num -= co_new * mon
    print(f"{co_new} монет по {mon} рублей")
    print("-" * 15)





