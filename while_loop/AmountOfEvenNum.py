num = int(input())  # variable for enter a number
i = 0  # counter

while num != 0:  # until 0
    if num % 2 == 0:  # detecting even number
        i += 1
    num = int(input())  # enter number again

print(i)
