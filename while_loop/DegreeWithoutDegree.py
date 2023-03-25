N = int(input())

degree = 2
i = 1
while degree <= N:
    degree *= 2
    i += 1
print (i-1, degree // 2)