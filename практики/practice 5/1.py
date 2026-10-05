early_gain = int(input("введите свой годовой доход: "))
print("налоговая ставка = 13%")
tax = 13 #налоговая ставка
final_tax = early_gain * tax / 100 #налог
end_gain = early_gain - final_tax #финальный доход(без налога)
print("сумма налога составляет: ", final_tax)
print(f"итоговая сумма зарплаты составляет: {end_gain:.2f}")