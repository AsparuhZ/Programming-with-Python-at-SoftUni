text = input()
summ = 0

for i in range(0, len(text)):
    if text[i] == "a":
        summ = summ + 1
    if text[i] == "e":
        summ = summ + 2
    if text[i] == "i":
        summ = summ + 3
    if text[i] == "o":
        summ = summ + 4
    if text[i] == "u":
        summ = summ + 5
print(summ)
