number_moves = int(input())

result = 0
invalid_numbers = 0
null_to_nine = 0
ten_to_nineteen = 0
twenty_to_twenty_nine = 0
thirty_to_thirty_nine = 0
forty_to_fifty = 0

point_1 = 0
points_2 = 0
points_3 = 0
points_4 = 0

for _ in range(number_moves):
    current_number = int(input())
    if current_number < 0:
        invalid_numbers += 1
        result = result / 2
    if 0 <= current_number <= 9:
        points_1 = current_number * 0.2
        result += points_1
        null_to_nine += 1
    elif 10 <= current_number <= 19:
        points_2 = current_number * 0.3
        result += points_2
        ten_to_nineteen += 1
    elif 20 <= current_number <= 29:
        points_3 = current_number * 0.4
        result += points_3
        twenty_to_twenty_nine += 1
    elif 30 <= current_number <= 39:
        result += 50
        thirty_to_thirty_nine += 1
    elif 40 <= current_number <= 50:
        result += 100
        forty_to_fifty += 1
    elif current_number > 50:
        invalid_numbers += 1
        result = result / 2

percentage_0_9 = null_to_nine / number_moves * 100
percentage_10_19 = ten_to_nineteen / number_moves * 100
percentage_20_29 = twenty_to_twenty_nine / number_moves * 100
percentage_30_39 = thirty_to_thirty_nine / number_moves * 100
percentage_40_50 = forty_to_fifty / number_moves * 100
percentage_invalid = invalid_numbers / number_moves * 100

print(f"{result:.2f}")
print(f"From 0 to 9: {percentage_0_9:.2f}%")
print(f"From 10 to 19: {percentage_10_19:.2f}%")
print(f"From 20 to 29: {percentage_20_29:.2f}%")
print(f"From 30 to 39: {percentage_30_39:.2f}%")
print(f"From 40 to 50: {percentage_40_50:.2f}%")
print(f"Invalid numbers: {percentage_invalid:.2f}%")
