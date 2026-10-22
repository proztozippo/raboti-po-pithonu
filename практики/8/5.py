list = []
num = int(input("введите число n: "))

for i in range(1, num + 1):
    num_int = int(input(f"введите {i} число из списка: "))
    list.append(num_int)
max_1 = max(list)
list.remove(max_1)
max_2 = max(list)
print("самое большое число: ", max_1, "второе по величине: ", max_2)