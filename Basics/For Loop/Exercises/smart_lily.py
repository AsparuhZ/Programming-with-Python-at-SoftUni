age = int(input())
price_laundry = float(input())
price_per_toy = int(input())
even_birthday = 0
total = 0
num_toys = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        even_birthday += 10
        total += even_birthday - 1
    else:
        num_toys += 1
total += num_toys * price_per_toy
difference = abs(total - price_laundry)

if total >= price_laundry:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
