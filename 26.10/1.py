a = 0
while True:
    passw = int(input("введите пароль: "))
    if passw == 1234:
        print("доступ разрешен")
    else:
        a += 1
    if a == 5:
        print("доступ запрещен")
        break