number = int(input())
left_summ = 0
right_summ = 0

for i in range(number):
    current_number = int(input())
    left_summ += current_number
for i in range(number):
    current_number = int(input())
    right_summ += current_number

if left_summ == right_summ:
    print(f" Yes, sum = {left_summ}")
else:
    difference = abs(left_summ - right_summ)
    print(f"No, diff = {difference}")
