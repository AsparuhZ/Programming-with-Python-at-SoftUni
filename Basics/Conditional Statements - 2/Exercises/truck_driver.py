season = input()
kilometer_month = float(input())

total = 0
price_per_km = 0
one_season_in_months = 4

if season == "Spring" or season == "Autumn":
    if kilometer_month <= 5000:
        price_per_km = 0.75
    elif 5000 < kilometer_month <= 10000:
        price_per_km = 0.95
    elif 10000 < kilometer_month <= 20000:
        price_per_km = 1.45

elif season == "Summer":
    if kilometer_month <= 5000:
        price_per_km = 0.90
    elif 5000 < kilometer_month <= 10000:
        price_per_km = 1.10
    elif 10000 < kilometer_month <= 20000:
        price_per_km = 1.45

elif season == "Winter":
    if kilometer_month <= 5000:
        price_per_km = 1.05
    elif 5000 < kilometer_month <= 10000:
        price_per_km = 1.25
    elif 10000 < kilometer_month <= 20000:
        price_per_km = 1.45

total = (kilometer_month * price_per_km) * one_season_in_months
final_summ = total - (total * 0.10)

print(f"{final_summ:.2f}")