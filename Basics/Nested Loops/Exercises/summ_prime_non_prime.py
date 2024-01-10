
is_prime = True
summ_prime = 0
summ_non_prime = 0

user_input = input()
while user_input != "stop":
    current_number = int(user_input)

    if current_number < 0:
        print("Number is negative.")

    else:

        for i in range(2,current_number):
            if current_number % i == 0:
                is_prime = False
                break

        if is_prime:
            summ_prime += current_number
        else:
            summ_non_prime += current_number
            is_prime = True

    user_input = input()

print(f"Sum of all prime numbers is: {summ_prime}")
print(f"Sum of all non prime numbers is: {summ_non_prime}")