# Given two numbers n and m. Create a two-dimensional array of size (n×m)
# and populate it with the characters "." and "*" in a checkerboard pattern.
# The top left corner should have the character "."

# read 2 space-separated values
row, elem = [int(i) for i in input().split()]
# create the array consisting from the dots
chess_desk = [["."] * elem for i in range(row)]

for i in range(0, row, 2):  # for odd rows
    for j in range(1, elem, 2):  # and even elements in row
        chess_desk[i][j] = "*"
for i in range(1, row, 2):  # for even rows
    for j in range(0, elem, 2):  # and odd elements in row
        chess_desk[i][j] = "*"

for i in chess_desk:  # for each row of the array
    print(" ".join([j for j in i]))  # display elements separated by space
