#курс рубля
rubles = 83.48
#перевод из доллара в рубль
def convert_rub_doll(dollars):
    dollars = dollars * rubles
    return dollars


#вводим сумму(в долларах)
dollars = float(input("Введите сумму в долларах: "))

#считаем
sum_rubles = convert_rub_doll(dollars)

print(f"{dollars:.2f} долларов = {sum_rubles:.2f} рублей")