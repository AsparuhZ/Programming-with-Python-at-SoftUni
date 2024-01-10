w = float(input())
h = float(input())

corridor = 100

width_hall = h * 100 - corridor
number_desks_for_row = width_hall // 70
length_hall = (w * 100)
number_row = length_hall // 120

counts_places = (number_desks_for_row * number_row) - 3

print(int(counts_places))