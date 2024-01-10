type_flower = input()
qty = int(input())
budget = int(input())
price_flower = 0

if type_flower == "Roses":
    price_flower = 5
    if qty > 80:
        price_flower *= 0.9

elif type_flower == "Dahlias":
    price_flower = 3.8
    if qty > 90:
        price_flower *= 0.85

elif type_flower == "Tulips":
    price_flower = 2.8
    if qty > 80:
        price_flower *= 0.85

elif type_flower == "Narcissus":
    price_flower = 3
    if qty < 120:
        price_flower *= 1.15

elif type_flower == "Gladiolus":
    price_flower = 2.5
    if qty < 80:
        price_flower *= 1.20

total_price = qty * price_flower
difference = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {qty} {type_flower} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")