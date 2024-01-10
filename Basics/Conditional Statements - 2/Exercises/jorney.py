budget = float(input())
season = input()

destination = ""
spent_money = 0
type_rest = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        spent_money = budget * 0.3
        type_rest = "Camp"
    elif season == "winter":
        spent_money = budget * 0.7
        type_rest = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        spent_money = budget * 0.4
        type_rest = "Camp"
    elif season == "winter":
        spent_money = budget * 0.8
        type_rest = "Hotel"
elif budget > 1000:
    destination = "Europe"
    spent_money = budget * 0.9
    type_rest = "Hotel"

print(f"Somewhere in {destination}")
print(f"{type_rest} - {spent_money:.2f}")
