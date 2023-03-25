num = int(input())  # variable for enter a number
num2 = 0  # variable for comparing

while num != 0:
    if num2 < num:  # operation of comparing
        num2 = num  # if entered number the largest then num2 = entered number
    num = int(input())  # enter number again
print(num2)
