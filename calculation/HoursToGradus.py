from math import *

H = int(input())
M = int(input())
S = int(input())


H2 = 360 / 12 * H
M2 = 360 / 12 * M / 60
S2 = 360 / 12 * S / 60 ** 2
print (fsum([H2, M2, S2]))
#print (sum([H2, M2, S2]))

