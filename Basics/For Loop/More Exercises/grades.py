number_students = int(input())

fail = 0
middle_grade = 0
good_grade = 0
excellent_grade = 0
total_grade = 0
for _ in range(number_students):
    current_grade = float(input())
    if 2 <= current_grade < 3:
        fail += 1
        total_grade += current_grade
    elif 3 <= current_grade < 4:
        middle_grade += 1
        total_grade += current_grade
    elif 4 <= current_grade < 5:
        good_grade += 1
        total_grade += current_grade
    elif current_grade >= 5:
        excellent_grade += 1
        total_grade += current_grade

average_grade = total_grade / number_students
percentage_fail = fail / number_students * 100
percentage_middle = middle_grade / number_students * 100
percentage_good_grade = good_grade / number_students * 100
percentage_excellent = excellent_grade / number_students * 100

print(f"Top students: {percentage_excellent:.2f}%")
print(f"Between 4.00 and 4.99: {percentage_good_grade:.2f}%")
print(f"Between 3.00 and 3.99: {percentage_middle:.2f}%")
print(f"Fail: {percentage_fail:.2f}%")
print(f"Average: {average_grade:.2f}")

