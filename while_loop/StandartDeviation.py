import math
sp = []
first = int(input())
brt = 0
while first != 0:
    sp.append(first)
    first = int(input())
s = sum(sp) / len(sp)
for i in range(len(sp)):
    brt += (sp[i] - s) ** 2
sigma = math.sqrt(brt / (len(sp)-1))
print(sigma)
