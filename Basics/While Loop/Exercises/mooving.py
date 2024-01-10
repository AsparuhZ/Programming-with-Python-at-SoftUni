width_app = int(input())
length_app = int(input())
high_app = int(input())
total_app = width_app * length_app * high_app
user_input = input()

while True:
    if user_input == "Done":
        print(f"{total_app} Cubic meters left.")
        break

    user_input = int(user_input)
    total_app -= user_input
    if total_app < 0:
        print(f"No more free space! You need {abs(total_app)} Cubic meters more.")
        break
    user_input = input()


