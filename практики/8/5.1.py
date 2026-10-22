max_1 = 0
max_2 = 0
num = int(input("введите количество чисел: "))
for i in range(1, num + 1):
    num_int = int(input(f"введите {i} число из списка: "))
    if num_int > max_1:
        max_1 = num_int
    elif num_int > max_2:
        max_2 = num_int
print("самое большое число: ", max_1, "второе по величине: ", max_2)