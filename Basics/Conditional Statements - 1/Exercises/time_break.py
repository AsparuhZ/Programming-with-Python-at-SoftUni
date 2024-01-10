from math import ceil
name_of_movie = input()
time_of_movie = int(input())
total_time = int(input())

time_for_lunch = total_time * 1/8
time_for_relax = total_time * 1/4

left_time = total_time - time_for_lunch - time_for_relax

extra_time = ceil(abs(left_time - time_of_movie))

if left_time >= time_of_movie:
    print(f"You have enough time to watch {name_of_movie} and left with {extra_time} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_movie}, you need {extra_time} more minutes.")
