start = int(input())
end = int(input())
magic_number = int(input())

count_combination = 0
is_enough = False

for a in range(start, end + 1):
    if is_enough:
        break
    for b in range(start, end + 1):
        if is_enough:
            break
        count_combination += 1
        if a + b == magic_number:
            is_enough = True
            print(f"Combination N:{count_combination} ({a} + {b} = {magic_number})")

if not is_enough:
    print(f"{count_combination} combinations - neither equals {magic_number}")