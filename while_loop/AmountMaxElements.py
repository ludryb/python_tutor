num = int(input())  # variable for enter a number
num2 = 0  # variable for comparing

while num != 0:
    if num2 < num:  # operation of comparing
         i = 1  # first maximum element
         num2 = num  # if entered number the largest then num2 = entered number
    num = int(input())  # enter number again
    if num2 == num:
        i += 1  # if entered number equal comparing variable, counting plus 1 max elements
print(i)
