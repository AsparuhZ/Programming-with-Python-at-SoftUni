from math import floor, ceil
days = int(input())
left_food = int(input())
dog_food_per_day_kg = float(input())
cat_food_per_day_kg = float(input())
turtle_food_per_day_gram = float(input())

total_dog = days * dog_food_per_day_kg
total_cat = days * cat_food_per_day_kg
total_turtle = (days * turtle_food_per_day_gram) / 1000

all_food_eaten = total_dog + total_cat + total_turtle
difference = abs(left_food - all_food_eaten)

if left_food >= all_food_eaten:
    print(f"{int(floor(difference))} kilos of food left.")
elif left_food < all_food_eaten:
    print(f"{int(ceil(difference))} more kilos of food are needed.")
