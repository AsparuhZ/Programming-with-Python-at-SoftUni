min_number = int(input())

while True:
    current_command = input()
    if current_command == "Stop":
        break

    number = int(current_command)

    if number < min_number:
        min_number = number


print(min_number)