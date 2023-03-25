a = [int(i) for i in input().split()]
# enter string with values separated by space
# using "split" u can recognize entering values
# it will string values instead numbers
# each value will convert to numbers with helps "int"
for i in range(len(a)):  # count amount of element in list
    if i % 2 == 0:  # taking each second element in list
        print(a[i], end=" ")  # print value each second element

