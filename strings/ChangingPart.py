import math

s = input()

x = math.ceil(len (s)/2)

a = s[:x]
b = s[x:]

print(b+a)