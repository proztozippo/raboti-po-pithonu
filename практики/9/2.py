count = 0
found_alexandra = False

while True:
    name = input("введите имя участника: ")
    if name == 'Александра':
        found_alexandra = True
    elif found_alexandra and name != 'Левон':
        count += 1
    elif name == 'Левон':
        break

print(f"между Александрой и Левоном {count} человек")
