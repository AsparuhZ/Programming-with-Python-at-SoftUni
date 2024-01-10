name = input()

total_grades = 0
years_count = 0
failed_years = 0

while True:
    current_grade = float(input())

    if current_grade < 4:
        failed_years += 1

        if failed_years == 2:
            current_failed_year = years_count + 1
            print(f"{name} has been excluded at {current_failed_year} grade")
            break
        continue

    years_count += 1
    total_grades += current_grade

    if years_count == 12:
        average_grade = total_grades / 12
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break
