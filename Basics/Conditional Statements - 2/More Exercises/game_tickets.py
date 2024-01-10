budget = float(input())
category = input()
number_people = int(input())

transport = 0
ticket = 0
total = 0

if 1 <= number_people <= 4:
    transport = budget * 0.75
elif 5 <= number_people <= 9:
    transport = budget * 0.6
elif 10 <= number_people <= 24:
    transport = budget * 0.5
elif 25 <= number_people <= 49:
    transport = budget * 0.4
elif number_people > 50:
    transport = budget * 0.25

if category == "VIP":
    ticket = 499.99

elif category == "Normal":
    ticket = 249.99

total = ticket * number_people + transport
difference = abs(budget - total)

if budget >= total:
    print(f"Yes! You have {difference:.2f} leva left.")
elif budget < total:
    print(f"Not enough money! You need {difference:.2f} leva.")
