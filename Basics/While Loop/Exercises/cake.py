length_cake = int(input())
width_cake = int(input())
user_input = input()

count_pieces_cake = length_cake * width_cake

while True:
    if user_input == "STOP":
        print(f"{count_pieces_cake} pieces are left.")
        break

    user_input = int(user_input)
    count_pieces_cake -= user_input
    if count_pieces_cake < 0:
        print(f"No more cake left! You need {abs(count_pieces_cake)} pieces more.")
        break
    user_input = input()
