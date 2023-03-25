v = int(input())
t = int(input())

if v > 0 or abs(v*t)%109 == 0:
    a = abs(v*t)%109
else:
    a = 109 - abs (v*t)%109

print (a)