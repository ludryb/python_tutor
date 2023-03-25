a = [int(i) for i in input().split()]
# entering values into a space-separated string
comp = a[0]  # taking the first value from the list to compare
for elem in a:  # for each element in the list
    if elem > comp:  # if it bigger than the compare variable
        print(elem, end=" ")  # print it value
    comp = elem  # change value of variable
