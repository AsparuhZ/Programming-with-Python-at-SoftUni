number = int(input())
even_summ = 0
odd_summ = 0

for i in range(0, number):
    current_number = int(input())
    if i % 2 == 0:
        even_summ += current_number
    else:
        odd_summ += current_number

if even_summ == odd_summ:
    print("Yes")
    print(f"Sum = {even_summ}")
else:
    diff = abs(even_summ - odd_summ)
    print("No")
    print(f"Diff = {diff}")
