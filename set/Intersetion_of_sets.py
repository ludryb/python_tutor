# Given two lists of numbers. Find all the numbers that occur in both the first and the second list
# and print them in ascending order.

# save the intersection between two lines of space-separated values
values = set(input().split()).intersection(set(input().split()))
# show sorted space-separated values
print(*sorted(values, key=int))
