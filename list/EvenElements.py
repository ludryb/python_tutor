a = [int(i) for i in input().split()]
# enter string with values separated by space
# using "split" u can recognize entering values
# it will string values instead numbers
# each value will convert to numbers with helps "int"
for i in a:  # sorting out each element in list
    if i % 2 == 0:  # if element division by 2
        print(i, end=" ")  # print element
