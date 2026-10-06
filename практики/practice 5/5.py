# Напишите программу, которая имитирует работу банкомата по выдаче наличных. Банкомат использует «жадный» алгоритм, т.е. всегда пытается выдать сначала самые крупные купюры.
# Задайте номиналы доступных купюр: B5000, B2000, B1000, B500, B200, B100.
sum = int(input())
num_5000 = 5000
num_2000 = 1000
num_1000 = 1000
num_500 = 500
num_200 = 200
num_100 = 100
print(f"выдача {sum} деняг")
print(sum)
print(sum // num_5000, "по 5000")
sum = sum - ((sum // num_5000) * num_5000)
print(sum)
print(sum // num_2000, "по 2000")
sum = sum - ((sum // num_2000) * num_2000)
print(sum)
print(sum // num_1000, "по 1000")
sum = sum - ((sum // num_1000) * num_1000)
print(sum)
print(sum // num_500, "по 500")
sum = sum - ((sum // num_500) * num_500)
print(sum)
print(sum // num_200, "по 200")
sum = sum - ((sum // num_200) * num_200)
print(sum)
print(sum // num_100, "по 100")
sum = sum - ((sum // num_100) * num_100)
print(sum)
print("остаток мелочью = ", sum % num_100)