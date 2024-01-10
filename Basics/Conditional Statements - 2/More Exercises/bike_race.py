juniors = int(input())
seniors = int(input())
type_trace = input()

price_junior = 0
price_seniors = 0
total_people = juniors + seniors

if type_trace == "trail":
    price_junior = 5.50
    price_seniors = 7

elif type_trace == "cross-country":
    if juniors + seniors >= 50:
        price_junior = 8 - (8 * 0.25)
        price_seniors = 9.50 - (9.50 * 0.25)
    else:
        price_junior = 8
        price_seniors = 9.50

elif type_trace == "downhill":
    price_junior = 12.25
    price_seniors = 13.75

elif type_trace == "road":
    price_junior = 20
    price_seniors = 21.50

total = (price_junior * juniors) + (price_seniors * seniors)

final_price = total - (total * 0.05)

print(f"{final_price:.2f}")
