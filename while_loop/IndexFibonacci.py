fn = int(input())  # enter number

n = 0  # current index of the sequence Fibonacci

f0, f1 = 1, 0  # current members of the sequence Fibonacci
if fn == 0:
    print("0")
elif fn == 1:  # Fibonacci sequence has two ones
    print("1 or 2")
else:  # for other members
    while f1 <= fn:  # count each member of the sequence before fn
        f0, f1 = f1, f0+f1  # at the beginning count f1 (next member of the sequence) after change prev member
        n += 1  # change index
    if fn % f1 == 0:  # sequence membership check 
        print(n)
    else:
        print(-1)
