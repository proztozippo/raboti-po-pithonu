a = 0
while True:
    inp = input("введите слово: ")
    if inp == "стоп" or inp == "хватит" or inp == "достаточно":
        break
    else:
        a += 1
print("количество слов:", a)