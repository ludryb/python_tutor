a = [int(i) for i in input().split()]
# enter values into a space-separated string and convert to integer
# i = 0  # cycle counter and index of list
# #while i < len(a)-1:
#    # while counter less than amount of elem in list
#    # amount of list is taken less one
#    # because we compare here previous values and next
#    prev = a[i]  # previous values
#    i += 1  # counter
#    next = a[i]  # next values
#    if prev < 0 and next < 0 or prev > 0 and next > 0:
#        # compare their sign and if it has the same sigh
#        print(prev, next)  # print values
#        break  # stop cycle
# similar second way which I like more
for i in range(len(a)-1): # from fist element to last but one
    if a[i] < 0 and a[i+1] < 0 or a[i] > 0 and a[i+1] > 0:
        print(a[i], a[i+1])
        break
