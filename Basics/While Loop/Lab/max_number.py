max_number = int(input())

while True:
    current_command = input()
    if current_command == "Stop":
        break

    number = int(current_command)

    if number > max_number:
        max_number = number


print(max_number)
