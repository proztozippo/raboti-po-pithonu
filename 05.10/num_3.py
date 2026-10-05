month = int(input("введите порядковый номер месяца"))
if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    print("31 day")
elif month == 4 or 6 or 9 or 11:
    print("30 days")
else:
    print("28 or 29")