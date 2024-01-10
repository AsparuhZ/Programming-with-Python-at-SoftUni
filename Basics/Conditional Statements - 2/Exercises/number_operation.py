number_one = int(input())
number_two = int(input())
operator = input()

total = 0
odd_or_even = 0
rest = 0

if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
        total = number_one + number_two
    elif operator == "-":
        total = number_one - number_two
    elif operator == "*":
        total = number_one * number_two
    if total % 2 == 0:
        odd_or_even = "even"
    else:
        odd_or_even = "odd"
    print(f"{number_one} {operator} {number_two} = {total} - {odd_or_even}")

elif operator == "/":
    if number_two == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        total = number_one / number_two
        print(f"{number_one} / {number_two} = {total:.2f}")


elif operator == "%":
    if number_two == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        rest = number_one % number_two
        print(f"{number_one} % {number_two} = {rest}")
