a = int(input())
b = int(input())
c = int(input())
d = int(input())

#if a - 1 == c and b - 1 == d or a + 1 == c and b + 1 == d:
#    print("YES")
#elif a - 1 ==c and b + 1 == d or a + 1 == c and b - 1 == d:
#if abs(a-c) == 1 and abs(b-d) == 1:
if abs(a - c) == abs(b-d):
    print("YES")
else:
    print("NO")

