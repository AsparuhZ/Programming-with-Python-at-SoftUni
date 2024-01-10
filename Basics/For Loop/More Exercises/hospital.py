period = int(input())
treated_patients = 0
untreated_patients = 0
number_doctors = 7

for day in range(1, period + 1):
    patients = int(input())
    if day % 3 == 0 and untreated_patients > treated_patients:
        number_doctors += 1
    if patients < number_doctors:
        treated_patients += patients
    else:
        treated_patients += number_doctors
    if patients > number_doctors:
        diff = patients - number_doctors
        untreated_patients += diff

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
