price_mackerel_kg = float(input())
price_sprinkle_kg = float(input())
bonito_in_kg = float(input())
safrid_in_kg = float(input())
mussels_in_kg = int(input())

price_bonito = price_mackerel_kg + (price_mackerel_kg * 0.60)
total_bonito = bonito_in_kg * price_bonito

price_safrid = price_sprinkle_kg + (price_sprinkle_kg * 0.80)
total_safrid = safrid_in_kg * price_safrid

price_mussels = 7.50
total_mussels = mussels_in_kg * price_mussels

total_summ = total_bonito + total_mussels + total_safrid
print(f"{total_summ:.2f}")
