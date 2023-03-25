import math

P = int (input())
X = int (input())
Y = int (input())

#Sum = (X + Y/100) * (X + Y/100)/100 * P
Sum = (X + Y/100) * (P / 100 + 1)
R = math.trunc(Sum)
K = math.trunc(round((Sum - int (R)), 2) *100)

print (R, K)