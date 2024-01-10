number = int(input())

summ_nummbers = 0

while True:
    current_number = int(input())
    summ_nummbers += current_number

    if summ_nummbers >= number:
        print(summ_nummbers)
        break

