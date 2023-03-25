x = int(input()) % 2 == 0
A = int(input()) % 2 == 0
y = int(input()) % 2 == 0
B = int(input()) % 2 == 0

# if x and A:
#     print("black")
# elif x or A:
#     print("white")
# # elif not (x or A):
# else:
#     print("black")


if x == A and y == B:
    print("YES")
elif not x == A and not y == B:
    print("YES")
# elif x and A and not y and not B:
#     print("black3")
# elif not x and not A and not (y and B):
#     print("black4")
else:
    print("YES")

