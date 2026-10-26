a = 0
num = []
while True:
    inp = input("введите число кратное семи: ")
    inp = int(inp)
    if inp % 7 == 0:
        a+=1
        num.append(inp)
    else:
        break
print("количество чисел: ", a, "числа: ", )
for i in num:
    print(i)