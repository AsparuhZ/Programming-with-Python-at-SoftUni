legacy_money = float(input())
year_to_live = int(input())
years_old = 18
total_money_spend = 0

for year in range(1800, year_to_live + 1):
    if year % 2 == 0:
        money_spend = 12000
    else:
        money_spend = 12000 + (years_old * 50)
    total_money_spend += money_spend
    years_old += 1

difference = abs(total_money_spend - legacy_money)

if total_money_spend > legacy_money:
    print(f"He will need {difference:.2f} dollars to survive.")
else:
    print(f"Yes! He will live a carefree life and will have {difference:.2f} dollars left.")
