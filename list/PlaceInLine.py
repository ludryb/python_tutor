a = [int(i) for i in input().split()]  # children height list
P = int(input())  # Peter's height
line = len(a)+1  # if cycle won't work then Peter stay at the end
for i in range(len(a)):  # from 0 to the numbers of element in list
    if a[i] < P:  # if Peter's height less than current
        line = i+1  # Peter's number in line
        break  # stop cycle
print(line)
