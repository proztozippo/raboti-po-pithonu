import random
print("угадай число от одного, до десяти включительно за 3 попыток")

b = random.choice(range(1, 11))

fff = 1
while True:
    if fff == 4:
        print("вы не уложились в 3 попытки")
        break
    a = int(input(f"попытка {fff}:"))
    if a == b and fff == 1:
        print("с первой попытки?...неплохо")
        print(f"число {b}, с {fff}-ого раза")
        break
    elif a == b and fff > 1:
        print(f"число {b}, с {fff}-ого раза")
        break
    elif a >= b:
        print("больше нужного")
        fff += 1
        continue
    elif a <= b:
        print("меньше нужного")
        fff += 1
        continue