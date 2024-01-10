from math import floor

number_tournaments = int(input())
start_points_rank = int(input())
total_points = start_points_rank
average_points = 0
wins = 0

for _ in range(number_tournaments):
    reached_point = input()
    if reached_point == "W":
        average_points += 2000
        total_points += 2000
        wins += 1
    elif reached_point == "F":
        average_points += 1200
        total_points += 1200

    elif reached_point == "SF":
        average_points += 720
        total_points += 720

percentage_wins = wins / number_tournaments * 100
average_points /= number_tournaments

print(f"Final points: {total_points}")
print(f"Average points: {int(floor(average_points))}")
print(f"{percentage_wins:.2f}%")
