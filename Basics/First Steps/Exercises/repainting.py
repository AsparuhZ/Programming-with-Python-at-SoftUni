amount_of_nylon: int = int(input())
amount_of_paint = int(input())
amount_of_thinner = int(input())
hours = int(input())

price_of_nylon = 1.5
price_of_paint = 14.5
price_of_thinner = 5
bags = 0.40

total_price_nylon = (amount_of_nylon + 2) * price_of_nylon
total_price_paint = (amount_of_paint * 1.1) * price_of_paint
total_price_thinner = amount_of_thinner * price_of_thinner

total_summ = total_price_thinner + total_price_paint + total_price_nylon + bags
price_for_workers = total_summ * (30 / 100)
final_summ = total_summ + price_for_workers * hours
print(float(final_summ))
