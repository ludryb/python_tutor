# Given an odd number integer n, produce a two-dimensional array of size (n×n).
# Fill each element with a single character string of "." . Then fill the middle
# row, the middle column and the diagnals with the single character
# string of "*" (an image of a snow flake).


n = int(input())  # enter the size of array
# build an array with a loop consisting of a dot
snowflake = [["."] * n for i in range(n)]
for row in range(n):  # from 0 to entered number
    snowflake[row][row] = "*"  # for the main diagonal
    snowflake[row][(n-1-row)] = "*"  # for second diagonal
    snowflake[row][(n-1)//2] = "*"  # for median column
    snowflake[(n-1)//2][row] = "*"  # for median row

for i in snowflake:  # for each row in the array
    print(" ".join([j for j in i]))  # each element will be separated by a space
