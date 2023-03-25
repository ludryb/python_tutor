# Given two positive integers m and n, m lines of n elements, giving an m×n matrix A, followed by
# two non-negative integers i and j less than n, swap columns i and j of A and print the result.


# read two space-separated values
row, elem = [int(i) for i in input().split()]
# read the array consisted by space-separated values
array = [[int(i) for i in input().split()] for j in range(row)]
# read the index of the columns to be swapped
# old index is "col" and new is "col_ch"
col, col_ch = [int(i) for i in input().split()]

for i in range(row):  # for row with the indices from 0 to row
    # swap elements with old element index and new index for each "i"-row
    array[i][col], array[i][col_ch] = array[i][col_ch], array[i][col]

for i in array:
    print(" ".join([str(j) for j in i]))
