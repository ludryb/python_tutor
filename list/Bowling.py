N, K = [int(i) for i in input().split()]

num = [i for i in range(1, N + 1)]
N = [i for i in range(1, N + 1)]

for i in range(K):
    li, ki = [int(i) for i in input().split()]
    for j in range(li - 1, ki):
        N[j] = "."
for i in range(len(N)):
    if N[i] in num:
        N[i] = "I"

print(*N, sep="")
