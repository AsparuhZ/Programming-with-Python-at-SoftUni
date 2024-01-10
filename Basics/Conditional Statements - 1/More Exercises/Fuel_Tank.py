type_fuel = input()
fuel_in_tank = float(input())
first_fuel = "diesel"
second_fuel = "gasoline"
third_fuel = "gas"
invalid_output = "Invalid fuel!"

if type_fuel == "Diesel":
    if fuel_in_tank >= 25:
        print(f"You have enough {first_fuel}.")
    elif fuel_in_tank < 25:
        print(f"Fill your tank with {first_fuel}!")
elif type_fuel == "Gasoline":
    if fuel_in_tank >= 25:
        print(f"You have enough {second_fuel}.")
    elif fuel_in_tank < 25:
        print(f"Fill your tank with {second_fuel}!")
elif type_fuel == "Gas":
    if fuel_in_tank >= 25:
        print(f"You have enough {third_fuel}.")
    elif fuel_in_tank < 25:
        print(f"Fill your tank with {third_fuel}!")

if type_fuel != "Diesel" and type_fuel != "Gasoline" and type_fuel != "Gas":
    print("Invalid fuel!")
