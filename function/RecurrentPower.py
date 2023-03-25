def power(a, n):
    if n == 0:
        a = 1
    else:
        a = a * a ** (n - 1)
    return a


print(power(float(input()), int(input())))

