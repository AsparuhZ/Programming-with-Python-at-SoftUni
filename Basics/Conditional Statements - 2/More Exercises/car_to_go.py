budget = float(input())
season = input()

type_class = ""
type_car = ""
price = 0

if budget <= 100:
    type_class = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        price = budget * 0.35
    elif season == "Winter":
        type_car = "Jeep"
        price = budget * 0.65

elif 100 < budget <= 500:
    type_class = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        price = budget * 0.45
    elif season == "Winter":
        type_car = "Jeep"
        price = budget * 0.80

elif budget > 500:
    type_class = "Luxury class"
    type_car = "Jeep"
    price = budget * 0.90


print(type_class)
print(f"{type_car} - {price:.2f}")
