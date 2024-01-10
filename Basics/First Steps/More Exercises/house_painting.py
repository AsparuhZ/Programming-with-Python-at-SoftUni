x = float(input())
y = float(input())
h = float(input())

side_wall = x * y
window = 1.5 * 1.5
area_side_walls = side_wall * 2 - 2 * window

front_door = 1.2 * 2
front_wall = x * x
front_and_back_walls = front_wall * 2 - front_door

total_size = area_side_walls + front_and_back_walls
painting_for_walls = total_size / 3.4

roof_side = x * y
area_roof_sides = roof_side * 2

area_roof_front = x * h / 2
roof_front_back = 2 * area_roof_front

total_area_roof = area_roof_sides + roof_front_back
painting_for_roof = total_area_roof / 4.3

print(f"{painting_for_walls:.2f}")
print(f"{painting_for_roof:.2f}")
