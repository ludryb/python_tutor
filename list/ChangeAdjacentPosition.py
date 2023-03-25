a = input().split()  # enter value a space-separated string

for i in range(0, len(a)-1, 2):  # for each second element in list
    # subtract one from length of the list
    # it helps to work with even amount length of the list
    # if we enter odd amount value, then length will be even
    # loop will take the last value and try to swap it with a void
    a[i+1], a[i] = a[i], a[i+1]

print(*a)
