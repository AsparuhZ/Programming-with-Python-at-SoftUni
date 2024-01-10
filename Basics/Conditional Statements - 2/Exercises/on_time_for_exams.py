hour_exam = int(input())
minute_exam = int(input())
hour_arriving = int(input())
minute_arriving = int(input())

time_of_exam = hour_exam * 60 + minute_exam
time_arriving = hour_arriving * 60 + minute_arriving

if time_arriving > time_of_exam:
    print("Late")
elif time_of_exam - 30 <= time_arriving <= time_of_exam:
    print("On time")
elif time_of_exam - 30 > time_arriving:
    print("Early")

difference = abs(time_of_exam - time_arriving)
hours = difference // 60
minutes = difference % 60

if time_of_exam - 60 < time_arriving < time_of_exam:
    print(f"{minutes} minutes before the start")
elif time_arriving <= time_of_exam - 60:
    print(f"{hours}:{minutes:02d} hours before the start")

elif time_of_exam < time_arriving < time_of_exam + 60:
    print(f"{minutes} minutes after the start")
elif time_arriving >= time_of_exam + 60:
    print(f"{hours}:{minutes:02d} hours after the start")
