price_holiday = float(input())
puzzles = int(input())
puppets = int(input())
tedy_bear = int(input())
minions = int(input())
truck = int(input())

#price_puzzle = 2.60
#price_puppets = 3
#price_bear = 4.10
#price_minions = 8.20
#price_truck = 2

number_toys = puzzles + puppets + tedy_bear + minions + truck
total_price = puzzles * 2.60 + puppets * 3 + tedy_bear * 4.10 + minions * 8.20 + truck * 2

if number_toys >= 50:
    total_price = total_price - (total_price * 0.25)

rent = total_price * 0.10
final_summ = total_price - rent
left_money = abs(final_summ - price_holiday)

if final_summ >= price_holiday:
    print(f"Yes! {left_money:.2f} lv left.")
else:
    print(f"Not enough money! {left_money:.2f} lv needed.")
