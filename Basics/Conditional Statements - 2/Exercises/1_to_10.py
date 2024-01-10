while True:
    number = float(input())
    if number < 0:
        print("Negative number!")
        break

    else:
        total = number * 2
        print(f"Result: {total:.2f}")
