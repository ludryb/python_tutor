first = int(input())  # first member of sequence for start cycle
i, k = 1, 1  # counter for cycle the biggest amount equal num (i) and counter for saving i-counter outside cycle
# when equal nums in sequence ended and begin different nums we need to

while first != 0:  # terms for end program
    second = int(input())  # second member of sequence
    if first == second:  # if it equals
        i += 1  # start counter
    elif k < i:  # if equal nums in sequence ended then compare saving-counter (k) and cycle-counter (i)
        k, i = i, 1  # if saving-counter (k) smaller than cycle-counter (i) then update "k" and reset "i"
    else:  # if equal nums in sequence ended and "k" bigger than "i" just reset "i"
        i = 1
    first = second  # save previous value for next compare
print(k)
