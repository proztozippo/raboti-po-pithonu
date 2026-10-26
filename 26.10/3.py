import random
print("угадай число от одного, до тысячи включительно")

b = random.choice(range(0, 1001))


fff = 1
while True:

    a = int(input(f"попытка {fff}:"))
    if a == b and fff == 1:
        print("с первой попытки?...неплохо")
        print(f"число {b}, с {fff}-ого раза")
        break
    elif a == b and fff == 2:
        print(f"число {b}, с {fff}-ого раза, тоже хорошо")
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