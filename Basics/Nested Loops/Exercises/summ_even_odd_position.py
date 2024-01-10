n1 = int(input())
n2 = int(input())


for num in range(n1, n2 + 1):

    first = num // 100000
    second = int(num / 10000) % 10
    third = int(num / 1000) % 10
    fourth = int(num / 100) % 10
    fifth = int(num / 10) % 10
    sixth = num % 10

    even_summ = first + third + fifth
    odd_summ = second + fourth + sixth

    if even_summ == odd_summ:
        print(num, end=" ")

