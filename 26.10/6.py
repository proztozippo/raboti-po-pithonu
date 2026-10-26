a = 0
while True:
    num = int(input("введите оценку"))
    if num == 5:
        a += 1
    elif num > 5 or num < 1:
        break
print(a, "пятерок")