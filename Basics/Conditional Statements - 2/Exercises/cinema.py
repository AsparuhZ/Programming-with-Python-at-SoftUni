type_movie = input()
rows = int(input())
columns = int(input())

total = 0

capacity = rows * columns

if type_movie == "Premiere":
    total = capacity * 12

elif type_movie == "Normal":
    total = capacity * 7.5

elif type_movie == "Discount":
    total = capacity * 5

print(f"{total:.2f}")
