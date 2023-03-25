def rec(n):
    a = 1
    if n < 4:
        print(n)
        rec(n+1)
        print(a + 2)

rec(0)

