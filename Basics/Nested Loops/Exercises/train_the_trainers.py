n = int(input())


all_grade = 0
grades_counter = 0

command = input()
while command != "Finish":
    grade = 0
    average_grade = 0

    for i in range(n):
        grade += float(input())
        grades_counter += 1

    average_grade = grade / n
    all_grade += grade
    print(f"{command} - {average_grade:.2f}.")

    command = input()

final_assessment = all_grade / grades_counter

print(f"Student's final assessment is {final_assessment:.2f}.")
