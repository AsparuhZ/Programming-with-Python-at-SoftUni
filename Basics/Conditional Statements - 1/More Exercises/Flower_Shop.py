from math import ceil, floor
qty_magnolia = int(input())
qty_hyacinth = int(input())
qty_roses = int(input())
qty_cactus = int(input())
price_gift = float(input())

price_magnolia = 3.25
price_hyacinth = 4
price_rose = 3.50
price_cactus = 8

total_magnolia = qty_magnolia * price_magnolia
total_hyacinth = qty_hyacinth * price_hyacinth
total_roses = qty_roses * price_rose
total_cactus = qty_cactus * price_cactus
summ = total_magnolia + total_hyacinth + total_roses + total_cactus
final_summ = summ - (summ * 0.05)

difference = abs(price_gift - final_summ)

if final_summ >= price_gift:
    print(f"She is left with {int(floor(difference))} leva.")
elif final_summ < price_gift:
    print(f"She will have to borrow {int(ceil(difference))} leva.")
