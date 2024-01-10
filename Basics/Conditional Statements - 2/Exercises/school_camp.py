season = input()
type_people = input()
number_students = int(input())
number_sleepover = int(input())

total = 0
price = 0
type_sport = ""

if season == "Winter":
    if type_people == "boys":
        price = 9.60
        type_sport = "Judo"
    elif type_people == "girls":
        price = 9.60
        type_sport = "Gymnastics"
    elif type_people == "mixed":
        price = 10
        type_sport = "Ski"

elif season == "Spring":
    if type_people == "boys":
        price = 7.20
        type_sport = "Tennis"
    elif type_people == "girls":
        price = 7.20
        type_sport = "Athletics"
    elif type_people == "mixed":
        price = 9.50
        type_sport = "Cycling"

elif season == "Summer":
    if type_people == "boys":
        price = 15
        type_sport = "Football"
    elif type_people == "girls":
        price = 15
        type_sport = "Volleyball"
    elif type_people == "mixed":
        price = 20
        type_sport = "Swimming"

total = number_students * number_sleepover * price

if 10 <= number_students < 20:
    total = total - (total * 0.05)
elif 20 <= number_students < 50:
    total = total - (total * 0.15)
elif number_students >= 50:
    total = total / 2

print(f"{type_sport} {total:.2f} lv.")