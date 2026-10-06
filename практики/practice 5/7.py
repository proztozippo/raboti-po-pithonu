travel_distance = float(input("введите дальность поездки в км"))
fuel_cons = float(input("введите расход топлива литров за км"))
fuel_cost = float(input("введите слоимость топлива в литрах"))

def travel_cost(travel_distance, fuel_cons, fuel_cost): # высчитываем стоимость поездки
    total_cost = travel_distance * fuel_cost * fuel_cons
    return total_cost


print("надо бензина: ", travel_distance * fuel_cons)
print("стоимость поездки: ", travel_cost(travel_distance, fuel_cons, fuel_cost))