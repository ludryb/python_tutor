a = input().split()  # enter values into space-separated string
pairs = 0  # counter for identical pairs
for i in range(len(a)):  # from 0 to length of the list
    pairs += a[i:len(a)].count(a[i]) - 1
    # count amount current element in list what started from "i"
    # subtracted one because count pair, not amount
print(pairs)
