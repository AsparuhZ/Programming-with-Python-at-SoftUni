num = int(input())


for i in range(1111, 10000):
    is_special = True

    num_to_string = str(i)
    for j in range(len(num_to_string)):
        current_number = int(num_to_string[j])
        if current_number == 0 or num % current_number != 0:
            is_special = False
            break


    if is_special:
        print(i, end=" ")
