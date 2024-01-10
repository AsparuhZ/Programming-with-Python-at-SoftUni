name_actor = input()
academy_points = float(input())
number_judges = int(input())
total_points = academy_points

for _ in range(number_judges):
    name_judge = input()
    points = float(input())
    current_points = len(name_judge) * points / 2
    total_points += current_points
    if total_points > 1250.5:
        break
if total_points > 1250.5:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    difference = abs(total_points - 1250.5)
    print(f"Sorry, {name_actor} you need {difference:.1f} more!")
