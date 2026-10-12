print(
    """
№   |напиток   | цена
1   |кофе ☕   |120 рублей
2   |чай 🍵    |80 рублей
3   |сок 🧃    |100 рублей
4   |вода 💦   |50 рублей
5   |лимонад 🍺|90 рублей
""")

num_dri = int(input("введите номер напитка: "))

match num_dri:
    case 1:
        cost_dri = 120
    case 2:
        cost_dri = 80
    case 3:
        cost_dri = 100
    case 4:
        cost_dri = 50
    case 5:
        cost_dri = 90

count_dri = int(input("введите количество напитков"))

print("скидки: \n"
      "1 для студентов\n"
      "2 для постоянных клиентов\n"
      "3 для новых клиентов\n")

sale_check = 0
sale_check = input("вам подходит один из вариантов скидок? да/нет \n")

match sale_check:
    case "да":
        code_sale = int(input("введите код скидки: "))
    case 0:
        print("ошибка вводимого значения, скидка не будет засчитана")
    case "нет":
        print("скидка отсутствует")


print("-" * 10)
print(f"вы заказали {num_dri} порции 🥤")
print(f"цена за одну порцию: {cost_dri}")
print(f"количество напитков: {count_dri}")

total = cost_dri * count_dri
print("итоговая сумма: ", total)

if code_sale == 1 or 2 or 3:
    print("скидка равна 20%")
    total = total - (total * 0.20)
print(f"окончательная сумма составляет {total} рублей")