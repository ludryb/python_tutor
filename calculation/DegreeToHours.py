import math

a = float (input())

H = a // 30
M = (a % 30) / 30 * 60
S = M % 1 * 60

print (round (H), math.floor (M), math.floor (S), sep = ":")
