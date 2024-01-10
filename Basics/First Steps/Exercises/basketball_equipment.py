tax_per_year = int(input())

price_shoes = tax_per_year - (tax_per_year * 0.4)
price_clothes = price_shoes - (price_shoes * 0.2)
price_ball = price_clothes / 4
price_accsessories = price_ball / 5

total_price = tax_per_year + price_shoes + price_clothes + price_ball + price_accsessories
print(float(total_price))
