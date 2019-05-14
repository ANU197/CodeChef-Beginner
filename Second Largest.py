"""
Three numbers A, B and C are the inputs. Write a program to find second largest among three numbers.

Input
The first line contains an integer T, total number of testcases. Then follow T lines, each line contains three integers A, B and C.

Output
Display the second largest among A, B and C.

Constraints
1 ≤ T ≤ 1000
1 ≤ A,B,C ≤ 1000000
Example
Input
3
120 11 400
10213 312 10
10 3 450

Output

120
312
10

"""
for i in range(int(input())):
    x = input().split(" ")
    a = int(x[0])
    b = int(x[1])
    c = int(x[2])

    if (a > b and a > c):
        if (b > c):
            print(b)
        else:
            print(c)
    elif (b > a and b > c):
        if (a > c):
            print(a)
        else:
            print(c)
    elif (c > a and c > b):
        if (a > b):
            print(a)
        else:
            print(b)

# # cook your dish here
# for i in range(int(input())):
#     x = input().split(" ")
#
#     if (int(x[0]) > int(x[1]) and int(x[0]) > int(x[2])):
#         if (int(x[1]) > int(x[2])):
#             print(int(x[1]))
#         else:
#             print(int(x[2]))
#     elif (int(x[1]) > int(x[0]) and int(x[1]) > int(x[2])):
#         if (int(x[0]) > int(x[2])):
#             print(int(x[0]))
#         else:
#             print(int(x[2]))
#     elif (int(x[2]) > int(x[0]) and int(x[2]) > int(x[1])):
#         if (int(x[0]) > int(x[1])):
#             print(int(x[0]))
#         else:
#             print(int(x[1]))