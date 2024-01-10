number_days = int(input())
type_room = input()
feedback = input()

price_room = 0
final_price = 0

if type_room == "room for one person":
    price_room = 18
    final_price = (number_days - 1) * price_room

elif type_room == "apartment":
    price_room = 25
    final_price = (number_days - 1) * price_room
    if number_days <= 10:
        final_price = final_price - (final_price * 0.30)
    elif number_days <= 15:
        final_price = final_price - (final_price * 0.35)
    elif number_days > 15:
        final_price = final_price - (final_price * 0.50)

if type_room == "president apartment":
    price_room = 35
    final_price = (number_days - 1) * price_room
    if number_days <= 10:
        final_price = final_price - (final_price * 0.10)
    elif number_days <= 15:
        final_price = final_price - (final_price * 0.15)
    elif number_days > 15:
        final_price = final_price - (final_price * 0.20)

if feedback == "positive":
    final_price = final_price + (final_price * 0.25)
elif feedback == "negative":
    final_price = final_price - (final_price * 0.10)

print(f"{final_price:.2f}")
