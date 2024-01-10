deposit_sum = float(input())
months_deposit = int(input())
year_fees_percent = float(input())
interest = deposit_sum * year_fees_percent / 100
per_month = interest / 12
summ = deposit_sum + months_deposit *  per_month
print(summ)
