number_loadings = int(input())

total_tones = 0
tones_bus = 0
tones_truck = 0
tones_train = 0

for _ in range(number_loadings):
    current_tones = int(input())
    if current_tones <= 3:
        tones_bus += current_tones
    elif 4 <= current_tones <= 11:
        tones_truck += current_tones
    elif 12 <= current_tones:
        tones_train += current_tones

total_tones = tones_bus + tones_truck + tones_train
average_per_tone = ((tones_bus * 200) + (tones_truck * 175) + (tones_train * 120)) / total_tones

percentage_bus = tones_bus / total_tones * 100
percentage_truck = tones_truck / total_tones * 100
percentage_train = tones_train / total_tones * 100

print(f"{average_per_tone:.2f}")
print(f"{percentage_bus:.2f}%")
print(f"{percentage_truck:.2f}%")
print(f"{percentage_train:.2f}%")
