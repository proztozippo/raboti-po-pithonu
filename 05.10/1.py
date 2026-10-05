mark = int(input("введите количество набранных баллов от 0 до 100: "))
print(mark, "баллов")
if mark >=90:
    print("оценка: 5")
elif 75 <= mark > 90:
    print("оценка: 4")
elif 60 <= mark > 75:
    print("оценка: 3")
else:
    print("оценка: 2")