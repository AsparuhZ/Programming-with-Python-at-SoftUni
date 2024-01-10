budget_movie = float(input())
number_statists = int(input())
price_clothes_one_statist = float(input())

decor = budget_movie * 0.10
total_price_clothes = number_statists * price_clothes_one_statist

if number_statists > 150:
    total_price_clothes = total_price_clothes - (total_price_clothes * 0.10)

price_decor_and_clothes = decor + total_price_clothes
money_needed = abs(price_decor_and_clothes - budget_movie)

if price_decor_and_clothes > budget_movie:
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")
elif price_decor_and_clothes <= budget_movie:
    print("Action!")
    print(f"Wingard starts filming with {money_needed:.2f} leva left.")
