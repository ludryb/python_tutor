a = [int(i) for i in input().split()]
# enter value into space-separated string and convert to numbers
maximum = a.index(max(a))  # search index of maximum
minimum = a.index(min(a))  # search index of minimum

a[maximum], a[minimum] = a[minimum], a[maximum]  # swap it
print(*a)