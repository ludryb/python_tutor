x = int(input())

a = x*45
b = x // 2 * 5
c = (x - 1 - x // 2) * 15

Hours = (a + b + c + 9*60) // 60
Minutes = (a + b + c + 9*60) % 60

print (Hours, ":", Minutes)