a = input().split()  # read first string
k, c = [int(i) for i in input().split()]
# assigning each variable a number
a.append(c)  # add variable "c" to the end of the list
for i in range(len(a)-1, k, -1):  # start enumeration from the end
    a[i], a[i-1] = a[i-1], a[i]   # move c-variable on k-position
    # for this we change positions two elements
    # current element will be last but one and move deep in the list
    # last but one element move to the end in the list
# one more interesting variant:
# a.append(0)
# a[k:]=[c]+a[k:len(a)]

print(*a)
