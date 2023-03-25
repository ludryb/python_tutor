N = int(input())
M = int(input())
x = int(input())
y = int(input())

if N < M:
    if x < N/2 and y < M/2:
        if x < y:
            print (x)
        else:
            print (y)
    elif x > N/2 and y < M/2:
        if y < (N-x):
            print (y)
        else:
            print (N-x)
    elif x > N/2 and y > M/2:
        if (N-x) < (M-y):
            print (N-x)
        else:
            print (M-y)
    else:
        if x < M-y:
            print (x)
        else:
            print (M-y)
else:
    if x < M / 2 and y < N / 2:
        if x < y:
            print(x)
        else:
            print(y)
    elif x > M / 2 and y < N / 2:
        if y < (M - x):
            print(y)
        else:
            print(M - x)
    elif x > M / 2 and y > N / 2:
        if (M - x) < (N - y):
            print(M - x)
        else:
            print(N - y)
    else:
        if x < N - y:
            print(x)
        else:
            print(N - y)




# if x < N/2 and x < M/2 and y < N/2 and y < M/2:
#     if x > y:
#         print(y)
#     else:
#         print(x)
# elif N > M:
#     if N/2 < x < y:
#         print(N - x)
#     else:  # N/2 < y < x
#         print(N - y)
# elif N < M:
#     if M/2 < x < y:
#         print(M - x)
#     else:  # M/2 < y < x
#         print(M - y)
# else:
#     print("Error")

# if N < M:
#     if x < y:
#         if x < M / 2:
#             print(x)
#         else:
#             print(M - x)
#     elif x > y:
#         if y < N / 2:
#             print(y)
#         else:
#             print(N-y)
# elif M > N:
#     if x < y:
#         if x < N / 2:
#             print(x)
#         else:
#             print(N - x)
#     elif x > y:
#         if y < M / 2:
#             print(y)
#         else:
#             print(M-y)
# else:
#     print("Error")
