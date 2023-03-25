num = int(input())  # variable for enter a number
num2 = 0  # variable for comparing
i = 0  # counter

while num != 0:
    if num2 < num:  # operation of comparing
        # if entered number the largest then num2 = entered number
        num2 = num
        l = i  # counter for maximum
    num = int(input())  # enter number again
    i += 1
print(l)
