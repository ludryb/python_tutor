a = int(input())
b = int(input())
c = int(input())

#print (min (a, b, c)) - faster way

if a < b and a < c:
    print(a)
elif b < c:
    print(b)
else:
    print(c)