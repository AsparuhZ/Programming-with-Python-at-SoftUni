number_pages = int(input())
pages_read_for_hour = int(input())
number_of_days = int(input())

pages_read_per_hours = number_pages / pages_read_for_hour
hours_per_day = pages_read_per_hours / number_of_days
print(int(hours_per_day))

