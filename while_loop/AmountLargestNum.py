num2 = int(input())  # first enter num
num = num2  # skip first cycle
i = 0  # counter

while num2 != 0:  # until 0
    if num2 > num:  # detecting the largest number
        i += 1  # remembering the largest
    num = num2  # remembering previous num
    num2 = int(input())  # enter new number
print(i)
