length_in_cm = int(input())
wight_in_cm = int(input())
height_in_cm = int(input())
filled_area_in_percentage = float(input())

size_of_tank = length_in_cm * wight_in_cm * height_in_cm
size_of_tank_in_liters = size_of_tank / 1000
liters_needed_filled = size_of_tank_in_liters - (size_of_tank_in_liters * filled_area_in_percentage / 100)

print(float(liters_needed_filled))
