x = int(input())  # first day distance
y = int(input())  # finally distance

i = 1  # day number

while x < y:
    x += 1.1  # distance is added 10% each day
    i += 1  # counter of days
print(i)
