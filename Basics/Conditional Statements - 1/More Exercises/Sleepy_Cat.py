day_off = int(input())
norm_per_year = 30000

time_if_off = day_off * 127
time_when_working = (365 - day_off) * 63
total_time = time_if_off + time_when_working

difference = abs(norm_per_year - total_time)
hours = difference // 60
minutes = difference % 60

if norm_per_year < total_time:
    print("Tom will run away")
    print(f" {hours} hours and {minutes} minutes more for play")

elif norm_per_year > total_time:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
