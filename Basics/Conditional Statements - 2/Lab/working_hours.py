time = int(input())
day = input()
user_output = ""

if day == "Monday":
    if 10 <= time <= 18:
        user_output = "open"
    else:
        user_output = "closed"

elif day == "Tuesday":
    if 10 <= time <= 18:
        user_output = "open"
    else:
        user_output = "closed"

elif day == "Wednesday":
    if 10 <= time <= 18:
        user_output = "open"
    else:
        user_output = "closed"

elif day == "Thursday":
    if 10 <= time <= 18:
        user_output = "open"
    else:
        user_output = "closed"

elif day == "Friday":
    if 10 <= time <= 18:
        user_output = "open"
    else:
        user_output = "closed"

elif day == "Saturday":
    if 10 <= time <= 18:
        user_output = "open"
    else:
        user_output = "closed"

elif day == "Sunday":
    user_output = "closed"

print(user_output)
