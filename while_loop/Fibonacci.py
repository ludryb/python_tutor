n = int(input())   # enter index Fibonacci-num
f0, f1 = 0, 1  # n-2, n-1
f2 = 0  # Fibonacci amount equal f0
i = 1  # current index

while i <= n:  # until the current index is equal to the entered index
    # start calculation Fibonacci num here
    f0, f1 = f1, f2  # equal to the next number sequence
    f2 = f0 + f1  # current Fibonacci amount
    i += 1  # current index

print(f2)
