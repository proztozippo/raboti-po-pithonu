import random

#ввод и рандомизация состояний посылки
stat = ["pending", "pocessing", "shiped", "delivered", "cancelled"]
a = random.randint(0, 4)
rand_stat =(stat[a])


print("-" * 30)
print("📦 статус вашего заказа 📦")
print("-" * 30)
print(f"статус: {rand_stat}")

#проверка на состояние заказа
match a:
    case 0:
        desc = ("заказ в ожидании")
        time = False
        rec = False
    case 1:
        desc = ("ваш заказ находится в обработке")
        time = False
        rec = False
    case 2:
        desc = ("отправлено")
        time = ("примерное время 2 - 5 дней")
        rec = ("крекомндуется: следите за уведомлениями о доставке")
    case 3:
        desc = ("доставлено")
        rec = ("рекомендуется забрать посылку в ближайшее время")
        time = False
    case 4:
        desc = ("отменено")
        time = False
        rec = ("возможно, на складе не оказалось вашей посылки"
               "попробуйте посмотреть посылку через время или ")
print(desc)

if time != False:
    print(time)

if rec != False:
    print(rec)