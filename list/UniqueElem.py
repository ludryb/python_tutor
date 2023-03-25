a = input().split()  # enter values into space-separated string
b = a.copy()  # list for loop

for i in b:  # for each element in list "b"
    if b.count(i) > 1:  # count amount of element "i" in list "b"
        # if it not unique element than remove it from list "a"
        a.remove(i)
# we use second list because after removing element
# it stops to be unique
print(*a)
