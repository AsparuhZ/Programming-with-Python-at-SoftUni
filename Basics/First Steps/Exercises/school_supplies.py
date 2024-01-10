numer_packages_pens = int(input())
number_packages_markers = int(input())
litres_of_chemical = int(input())
percent_of_disount = int(input())

price_package_pens = 5.80
price_package_markers = 7.20
price_per_litre_chemical = 1.20
discount_price_for_annie = percent_of_disount / 100

total_price_pens = numer_packages_pens * price_package_pens
total_price_markers = number_packages_markers * price_package_markers
total_price_for_litters = litres_of_chemical * price_per_litre_chemical
total_summ = total_price_for_litters + total_price_markers + total_price_pens
final_sum = total_summ - (total_summ * discount_price_for_annie)


print(final_sum)
