ran = range(0, 21)
for i in range(2, 20, 2):
    print(i)

for i in range(0, 21): #best
    if i % 2 == 0:
        print(i)
    continue

for i in ran:
    if i % 2 == 0:
        print(i)
    else:
        continue