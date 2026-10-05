check_1 = input("вы член? да/нет ")
if check_1 == "да":
    print("проходите")
else:
    check_2 = input("вам есть 18? да/нет ")
    if check_2 == "нет":
        print("вам нельзя")
    else:
        check_3 = input("предъявите документ\nпредъявил/нет ")
        if check_3 == "предъявил":
            print("проходите")
        else:
            print("доступ запрещен")