from math import *

h = int(input())
a = int(input())
b = int(input())

#S =  (h - a) / (a - b)
#S = a + 7 * (a - b)
S = (h - a) / (a - b) + 1


print (ceil(S))