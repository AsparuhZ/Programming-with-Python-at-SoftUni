import sys

number = int(input())
max_number = -sys.maxsize
total = 0

for _ in range(number):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    total += current_number

total = total - max_number

if max_number == total:
    print("Yes")
    print(f"Sum = {total}")
else:
    diff = abs(max_number - total)
    print("No")
    print(f"Diff = {diff}")
