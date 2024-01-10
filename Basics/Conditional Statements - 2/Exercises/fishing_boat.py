budget = int(input())
season = input()
number_people = int(input())

rent = 0

if season == "Spring":
    rent = 3000
elif season == "Summer" or season == "Autumn":
    rent = 4200
elif season == "Winter":
    rent = 2600

if number_people <= 6:
    rent = rent - (rent * 0.10)
elif number_people <= 11:
    rent = rent - (rent * 0.15)
elif number_people > 12:
    rent = rent - (rent * 0.25)

if number_people % 2 == 0 and season != "Autumn":
    rent = rent - (rent * 0.05)

difference = abs(budget - rent)

if budget >= rent:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
