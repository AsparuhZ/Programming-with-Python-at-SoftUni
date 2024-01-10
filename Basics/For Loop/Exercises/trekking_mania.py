number_groups = int(input())
musala = 0
moblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
total_people = 0
for num in range(number_groups):
    current_climbers = int(input())
    total_people += current_climbers
    if current_climbers <= 5:
        musala += current_climbers
    elif 6 <= current_climbers <= 12:
        moblan += current_climbers
    elif 13 <= current_climbers <= 25:
        kilimandjaro += current_climbers
    elif 26 <= current_climbers <= 40:
        k2 += current_climbers
    elif current_climbers >= 41:
        everest += current_climbers

musala_percentage = musala / total_people * 100
moblan_percentage = moblan / total_people * 100
kilimandjaro_percentage = kilimandjaro / total_people * 100
k2_percentage = k2 / total_people * 100
everest_percentage = everest / total_people * 100

print(f"{musala_percentage:.2f}%")
print(f"{moblan_percentage:.2f}%")
print(f"{kilimandjaro_percentage:.2f}%")
print(f"{k2_percentage:.2f}%")
print(f"{everest_percentage:.2f}%")
