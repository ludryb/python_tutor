a = [int(i) for i in input().split()]
# enter values into a space-separated string and convert to integer
amt = 0  # counter of the number elements is greater than neighbors
for i in range(1, len(a)-1):  # start from second element
    # finish lust but one, because we compare 3 elements
    if a[i-1] < a[i] > a[i+1]:
        # current elem greater than prev and next
        amt += 1  # plus 1 for counter
print(amt)
