number_of_day = int(input())
user_output = "Error"

if number_of_day == 1:
    user_output = "Monday"
elif number_of_day == 2:
    user_output = "Tuesday"
elif number_of_day == 3:
    user_output = "Wednesday"
elif number_of_day == 4:
    user_output = "Thursday"
elif number_of_day == 5:
    user_output = "Friday"
elif number_of_day == 6:
    user_output = "Saturday"
elif number_of_day == 7:
    user_output = "Sunday"

print(user_output)