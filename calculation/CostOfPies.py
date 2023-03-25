a = int(input())
b = int(input())
n = int(input())

K = n * b % 100
R1 = n * b // 100
R = R1 + n * a

print (R, K, sep = ".")