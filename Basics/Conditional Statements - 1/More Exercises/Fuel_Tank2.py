type_fuel = input()
qty_fuel = float(input())
club_card = input()

price_gasoline = 2.22
price_diesel = 2.33
price_gas = 0.93
total = 0

if type_fuel == "Gasoline":
    if club_card == "No":
        total = price_gasoline * qty_fuel
    elif club_card == "Yes":
        price_gasoline = price_gasoline - 0.18
        total = price_gasoline * qty_fuel

elif type_fuel == "Diesel":
    if club_card == "No":
        total = price_diesel * qty_fuel
    elif club_card == "Yes":
        price_gasoline = price_diesel - 0.12
        total = price_gasoline * qty_fuel

elif type_fuel == "Gas":
    if club_card == "No":
        total = price_gas * qty_fuel
    elif club_card == "Yes":
        price_gasoline = price_gas - 0.08
        total = price_gasoline * qty_fuel

if 20 <= qty_fuel <= 25:
    total = total - (total * 0.08)
elif qty_fuel > 25:
    total = total - (total * 0.1)

print(f"{total:.2f} lv.")
