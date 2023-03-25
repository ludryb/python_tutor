n = 20
for i in range(2, n):
    if (i == 2 or i == 3) or (i % 2 != 0 and i % 3 != 0):
        print(i)
