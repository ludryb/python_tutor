s = input()

f = ""
for i in range(len(s)):
    if i % 3 != 0:
        f+=s[i]
print (f)