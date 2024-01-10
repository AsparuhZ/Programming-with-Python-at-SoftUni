price_veg = float(input())
price_fruit = float(input())
kg_veg = int(input())
kg_fruit = int(input())
total_price_Euro = ((price_veg * kg_veg) + (price_fruit * kg_fruit)) / 1.94
print(f"{total_price_Euro:.2f}")
