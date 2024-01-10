kilometers = int(input())
time_of_day = input()

fee_taxi = 0.70
price_taxi_km = 0
price_bus_km = 0
price_train_km = 0
total = 0

if kilometers < 20:
    if time_of_day == "day":
        price_taxi_km = 0.79
        total = fee_taxi + (kilometers * price_taxi_km)
    elif time_of_day == "night":
        price_taxi_km = 0.90
        total = fee_taxi + (kilometers * price_taxi_km)

elif kilometers < 100:
    price_bus_km = 0.09
    total = kilometers * price_bus_km
elif kilometers >= 100:
    price_train_km = 0.06
    total = kilometers * price_train_km

print(f"{total:.2f}")
