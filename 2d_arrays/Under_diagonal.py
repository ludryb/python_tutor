# Given an integer n, create a two-dimensional array of size (n×n) and
# populate it as follows, with spaces between each character:
# The positions on the minor diagonal (from the upper right to the lower
# left corner) receive 1 .
# The positions above this diagonal recieve 0 .
# The positions below the diagonal receive 2 .

row_el = int(input())
# build an array with a loop, from 0 to the entered number
# the number of "0" will decrease by 1 in each row
# "1" belong minor diagonal and the number remains constant
# the number of "2" will increase by 1 starting from the second row
array = [[0]*(row_el-1-i) + [1] + [2]*i for i in range(row_el)]

for i in array:  # for each row in array
    print(" ".join([str(j) for j in i]))  # each element in row convert to string type and display
