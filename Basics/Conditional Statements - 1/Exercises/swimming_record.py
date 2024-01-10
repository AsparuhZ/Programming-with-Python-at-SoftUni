from math import floor
record_in_seconds = float(input())
length_in_meters = float(input())
time_in_seconds_per_meter = float(input())

total_seconds = length_in_meters * time_in_seconds_per_meter

number_of_delays = floor(length_in_meters / 15)
seconds_per_delay = 12.5

delay_in_seconds = (number_of_delays * seconds_per_delay)

total_summ_seconds = (total_seconds + delay_in_seconds)

time_difference = abs(record_in_seconds - total_summ_seconds)


if total_summ_seconds < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_summ_seconds:.2f} seconds.")
else:
    print(f"No, he failed! He was {time_difference:.2f} seconds slower.")