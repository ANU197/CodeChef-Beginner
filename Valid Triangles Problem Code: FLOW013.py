"""
Write a program to check whether a triangle is valid or not, when the three angles of the triangle are the inputs.
A triangle is valid if the sum of all the three angles is equal to 180 degrees.

Input
The first line contains an integer T, total number of testcases.
Then follow T lines, each line contains three angles A, B and C of triangle separated by space.

Output
Display 'YES' or 'NO' if the triangle is Valid or not respectively.

Constraints
1 ≤ T ≤ 1000
1 ≤ A,B,C ≤ 180
Example
Input

3
40 40 100
45 45 90
180 1 1
Output

YES
YES
NO

"""





for i in range(int(input())):
    x = input().split(" ")
    a = int(x[0])
    b = int(x[1])
    c = int(x[2])

    if a + b + c == 180 :
        print("YES")
    else:
        print("NO")
