from math import ceil, floor

area = int(input())
grape_per_one_qm = float(input())
litters_wine_needed = int(input())
workers = int(input())

total_grape = area * grape_per_one_qm
wine = (total_grape * 0.40) / 2.5

difference = abs(wine - litters_wine_needed)
litter_per_worker = difference / workers

if wine < litters_wine_needed:
    print(f"It will be a tough winter! More {int(floor(difference))} liters wine needed.")

elif wine >= litters_wine_needed:
    print(f"Good harvest this year! Total wine: {int(floor(wine))} liters.")
    print(f"{int(ceil(difference))} liters left -> {int(ceil(litter_per_worker))} liters per person.")
