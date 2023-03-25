def power(a, n):
    pow_num = 1
    if n > 0:
        for i in range(n):
            pow_num *= a
    else:
        for i in range(abs(n)):
            pow_num *= 1/a
    return pow_num


print(f'{power(float(input()), int(input())):.9}')
