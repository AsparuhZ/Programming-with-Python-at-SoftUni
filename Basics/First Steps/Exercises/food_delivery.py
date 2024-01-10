number_chicken_menus = int(input())
number_fish_menus = int(input())
number_veggie_menus = int(input())

price_per_chicken_menu = 10.35
price_per_fish_menu = 12.40
price_per_veggie_menu = 8.15
delivery = 2.50

total_price_chicken_menus = number_chicken_menus * price_per_chicken_menu
total_price_fish_menus = number_fish_menus * price_per_fish_menu
total_price_veggie_menus = number_veggie_menus * price_per_veggie_menu
final_price_menus = total_price_veggie_menus + total_price_fish_menus + total_price_chicken_menus
desert_price = final_price_menus * (20 / 100)
final_summ = final_price_menus + desert_price + delivery
print(float(final_summ))
