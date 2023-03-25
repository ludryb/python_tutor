a = int(input())
b = int(input())
c = int(input())
d = int(input())

#if (a+1 == c or a-1 == c or a == c) and (b-1 == d
#    or b+1 == d or b == d):
if a-1 <= c <= a+1 and b-1 <= d <= b+1:
    print("YES")
else:
    print("NO")

