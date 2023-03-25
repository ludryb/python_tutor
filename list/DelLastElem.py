a = input().split()  # enter values into a space-separated string
k = int(input())  # enter index element what we want remove
# a.append(a[k])  # add element with index "k" to the end
# a.remove(a[k])  # remove element with index "k"
for i in range(k, len(a)-1):
    # enumeration element start from element with index "k"
    a[i] = a[i+1]  # current element become next element
a.pop()  # remove last element
print(*a)
