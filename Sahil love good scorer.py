"""
Sahil is in the mood to attend Geeks Classes. He reaches venue of Geeks Classess. Now, he is confused about his sitting place. There are two columns of students sitting in the classes. Each student has been assigned a score on the basis of their score in Geeks Class Entrance Contest. Now, he wants to sit in the row which contains students with maximum score. Help him in finding the desired column.

Input : First line of Input contains testcase "T". For each testcase "T", there will be 3 lines of input, first line contains lengths of the columns, and next two lines contains the scores of students sitting in that column.

Output : For each testcase, Output the column in which Sahil should sit.

Constraints :
1 <= T <= 100
1 <= N1, N2 <= 10000
1 <= score <= 1000000

Example :
Input :
2
5 6
8 4 5 6 7
2 3 4 5 6 7
3 5
100 29 37
100 200 300 400 500
Output :
C1
C2

"""
# code


for z in range(int(input())):
    c = 0
    d = 0
    x = input().split(" ")
    y = input().split(" ")
    z = input().split(" ")
    for i in range(int(x[0])):
        c = c + int(y[i])
    for j in range(int(x[1])):
        d = d + int(z[j])

    if (c > d):
        print("C1")
    else:
        print("C2")


