A = int(input())
B = int(input())

l = list()

for i in range (A, B-1, -1):
    i *= i % 2
#    print (i)
    l.append(i)
    for i in range(l.count(0)):
        l.remove(0)
print (l)
#print (len(l))