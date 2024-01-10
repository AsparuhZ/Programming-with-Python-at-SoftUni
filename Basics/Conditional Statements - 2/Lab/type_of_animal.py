animal = input()

user_output = "unknown"

if animal == "dog":
    user_output = "mammal"

if animal == "crocodile" or animal == "tortoise" or animal == "snake":
    user_output = "reptile"

print(user_output)