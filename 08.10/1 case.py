num = int(input("введите свою оценку по пятибальной шкале: "))

match num:
    case 5:
        print("отличная работа *(^o^)*")
    case 4:
        print("хорошая работа")
    case 3:
        print("нормально")
    case 2:
        print("плохо")
    case _:
        print("некорректное значение")
