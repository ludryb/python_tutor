# Given a sequence of numbers, determine if the next number has already been encountered.
# For each number, print the word YES (in a separate line) if this number has already been
# encountered, and print NO, if it has not already been encountered.

empty_val = set()  # empty set for unique values
for i in input().split():  # for each space-separated value
    if i in empty_val:  # check if values belongs to the set
        print("YES")
    else:
        print("NO")
        empty_val.add(i)    
