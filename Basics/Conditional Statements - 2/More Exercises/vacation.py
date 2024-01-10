budget = float(input())
season = input()

location = ""
type_rest = ""
price = 0

if budget <= 1000:
    type_rest = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.45

elif 1000 < budget <= 3000:
    type_rest = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.60

elif budget > 3000:
    type_rest = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.90
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.90

print(f"{location} - {type_rest} - {price:.2f}")
