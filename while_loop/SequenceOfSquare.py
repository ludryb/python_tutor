N = int(input())

# for i in range(N):
#     i **= 2
#     if i == 0:
#         continue
#     if N < i:
#         break
#     print (i)

N = int(input())

sq, i = 1, 1

while N > sq:
    print (sq, end = " ")
    i += 1
    sq = i ** 2