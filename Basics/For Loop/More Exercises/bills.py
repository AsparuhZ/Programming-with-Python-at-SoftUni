number_months = int(input())

electricity = 0
water = 0
wlan = 0

price_water = 20
price_wlan = 15
total = 0
another_bills = 0

for _ in range(number_months):
    current_bill_electricity = float(input())
    electricity += current_bill_electricity
    water += price_water
    wlan += price_wlan
    total = current_bill_electricity + price_water + price_wlan
    another_bills += total + (total * 0.2)

average_per_month = (electricity + water + wlan + another_bills) / number_months

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {wlan:.2f} lv")
print(f"Other: {another_bills:.2f} lv")
print(f"Average: {average_per_month:.2f} lv")
