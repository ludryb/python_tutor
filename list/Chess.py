ver, hor = [int(i) for i in input().split()]
check = "NO"
S = []

while len(S) < 14 and check != "YES":
    S.append(ver)
    S.append(hor)
    ver, hor = [int(i) for i in input().split()]
    for j in range(0, len(S), 2):
        if S[j] == ver or S[j+1] == hor or (abs(S[j] - ver) == abs(S[j+1] - hor)):
            check = "YES"
            break

print(check)
