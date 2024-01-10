change = float(input())
change = int(change * 100)
coin_counter = 0

while change > 0:
    if change >= 200:
        change -= 200
        coin_counter += 1
    elif change >= 100:
        change -= 100
        coin_counter += 1
    elif change >= 50:
        change -= 50
        coin_counter += 1
    elif change >= 20:
        change -= 20
        coin_counter += 1
    elif change >= 10:
        change -= 10
        coin_counter += 1
    elif change >= 5:
        change -= 5
        coin_counter += 1
    elif change >= 2:
        change -= 2
        coin_counter += 1
    elif change >= 1:
        change -= 1
        coin_counter += 1

print(coin_counter)
