town = input()
trade = float(input())
commission = "error"

wrong_data = False

if town == "Sofia":
    if 0 <= trade <= 500:
        commission = trade * 0.05
    elif 500 < trade <= 1000:
        commission = trade * 0.07
    elif 1000 < trade <= 10000:
        commission = trade * 0.08
    elif 1000 < trade:
        commission = trade * 0.12
    else:
        wrong_data = True

elif town == "Varna":
    if 0 <= trade <= 500:
        commission = trade * 0.045
    elif 500 < trade <= 1000:
        commission = trade * 0.075
    elif 1000 < trade <= 10000:
        commission = trade * 0.1
    elif 10000 < trade:
        commission = trade * 0.13
    else:
        wrong_data = True

elif town == "Plovdiv":
    if 0 <= trade <= 500:
        commission = trade * 0.055
    elif 500 < trade <= 1000:
        commission = trade * 0.08
    elif 1000 < trade <= 10000:
        commission = trade * 0.12
    elif 10000 < trade:
        commission = trade * 0.145
    else:
        wrong_data = True
else:
    wrong_data = True

if not wrong_data:
    print(f"{commission:.2f}")
else:
    print("error")
