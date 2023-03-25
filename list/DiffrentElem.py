a = input().split()  # enter value into space-separated string
count = 0  # counter for numbers of different values
prev = ''  # compare variables
for i in range(len(a)):  # count the numbers of elements
    # and repeat as many times
    if prev != a[i]:  # comparing 'prev' and current elements
        count += 1  # if they not same add 1 in counter
        prev = a[i]  # change variable for compare
print(count)
