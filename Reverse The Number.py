"""
If an Integer N, write a program to reverse the given number.

Input
The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

Output
Display the reverse of the given number N.

Constraints
1 ≤ T ≤ 1000
1 ≤ N ≤ 100000
Example
Input
4
12345
31203
2123
2300
Output
54321
30213
3212
32

"""
# for i in range(int(input())):
#     x = input()
#     y = list(reversed(x))
#     print(y)




t = int(input())
for j in range(t):
    def firstlast(n):
        sum = 0
        x = len(n)
        for i in range(x):
            sum = sum*10 + int(n[x-i-1])

        return sum


    x = input()
    result = firstlast(x)
    print(int(result))

