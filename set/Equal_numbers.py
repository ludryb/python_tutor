# Given two lists of numbers. Count how many unique numbers occur in both of them.

# read two lines and save the same elements
values = set(input().split()).intersection(set(input().split()))
print(len(values))
