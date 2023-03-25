# Given two integers representing the rows and columns (m×n), and subsequent m rows of n elements,
# find the index position of the maximum element and print two numbers representing the index (i×j)
# or the row number and the column number. If there exist multiple such elements in different rows,
# print the one with smaller row number.


n, m = [int(i) for i in input().split()]  # reading 2 number for determine the size of an array
array = [int(i) for i in input().split(" ")]  # reading first line of the array
maximum = max(array)  # finding the biggest value
row, col = 0, array.index(maximum)  # finding indexes of the row and column of the biggest value
for each in range(1, n):  # starting from the second line because the first line was read before
    array = [int(i) for i in input().split(" ")]  # reading the row of space-separated values
    if max(array) > maximum:  # if the maximum of the new line greater than the previous maximum
        row, col = each, array.index(max(array))  # then change indexes of the greater value
        maximum = max(array)  # and save new maximum

print(row, col)  # display indexes of the greater value from array
