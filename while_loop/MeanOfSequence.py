num = 1  # variable for enter a number; 1 for enter a cycle
amount = 0  # sum sequence
i = 0  # counter of number

while num != 0:
    num = int(input())  # enter a number
    amount += num  # count sum
    i += 1  # count numbers
print(amount/(i-1))
