total = 0

while True:
    command = input()

    if command == "NoMoreMoney":
        break

    current_sum = float(command)

    if current_sum >= 0:
        total += current_sum
        print(f"Increase: {current_sum:.2f}")
    else:
        print("Invalid operation!")
        break

print(f"Total: {total:.2f}")
