chet = 0
nechet = 0
num = int(input("введите число: "))
for i in range(1, num + 1):
    if i % 2 == 0:
        chet += i
    else:
        nechet += i
end_sum = nechet - chet
print(f"результат вычисления знакопеременной суммы: \n            ==={end_sum}===")