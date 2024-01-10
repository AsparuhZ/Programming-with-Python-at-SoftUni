month = input()
number_nights = int(input())
s_price = 0
a_price = 0


if month == "May" or month == "October":
    s_price = 50
    a_price = 65
    if 7 < number_nights < 14:
        s_price *= 0.95
    elif 14 < number_nights:
        s_price *= 0.70
        a_price *= 0.90
elif month == "June" or month == "September":
    s_price = 75.20
    a_price = 68.70
    if number_nights > 14:
        s_price = s_price - (s_price * 0.2)
        a_price = a_price - (a_price * 0.10)
elif month == "July" or month == "August":
    s_price = 76
    a_price = 77
    if number_nights > 14:
        a_price = a_price - (a_price * 0.10)

total_studio = s_price * number_nights
total_apartment = a_price * number_nights

print(f"Apartment: {total_apartment:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")
