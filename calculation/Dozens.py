x = int(input())

Dozen = x % 10
Hundr = x // 10 % 10
Thous = x // 100 % 100

Sum = Dozen + Hundr + Thous

print (Sum)