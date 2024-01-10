n = int(input())

current_number = 1
is_finished = False

for rows in range(1, n + 1):
    for columns in range(1, rows + 1):
        if current_number > n:
            is_finished = True
            break

        print(current_number, end=" ")

        current_number += 1

    if is_finished:
        break
    print()