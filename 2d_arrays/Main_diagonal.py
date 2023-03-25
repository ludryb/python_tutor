# Given an integer n, produce a two-dimensional array of size (n×n)
# and complete it according to the following rules, and print
# with a single space between characters:
# On the main diagonal write 0 .
# On the diagonals adjacent to the main, write 1 .
# On the next adjacent diagonals write 2 and so forth.


row_el = int(input())  # enter the size of the array
# each row is filled with the difference between the element index and
# the row index, this difference is taken with the modulus
array = [[abs(elem-row) for elem in range(row_el)] for row in range(row_el)]

for row in array:  # for each row in the array
    print(" ".join([str(el) for el in row]))  # convert the element to the string and display
