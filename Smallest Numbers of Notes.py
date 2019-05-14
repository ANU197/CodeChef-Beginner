"""
Consider a currency system in which there are notes of seven denominations, namely, Rs. 1, Rs. 2, Rs. 5, Rs. 10, Rs. 50, Rs. 100.
If the sum of Rs. N is input, write a program to computer smallest number of notes that will combine to give Rs. N.

Input
The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

Output
Display the smallest number of notes that will combine to give N.

Constraints
1 ≤ T ≤ 1000
1 ≤ N ≤ 1000000
Example
Input
3
1200
500
242

Output
12
5
7

"""
# for i in range(int(input())):
#     import math
#
#     rs = int(input())
#     a = [100, 50, 10, 5, 2, 1]
#     b = 0
#     c = 0
#     d = 0
#     e = 0
#     f = 0
#     g = 0
#     # print(a)
#     # print(a[0])
#     # print(type(a))
#     # print(type(a[0]))
#
#     while (rs > a[0]):
#         b = rs / a[0]
#         rs = rs % a[0]
#         break
#
#     while (rs > a[1]):
#         c = rs / a[1]
#         rs = rs % a[1]
#         break
#
#     while (rs > a[2]):
#         d = rs / a[2]
#         rs = rs % a[2]
#         break
#
#     while (rs > a[3]):
#         e = rs / a[3]
#         rs = rs % a[3]
#         break
#
#     while (rs > a[4]):
#         f = rs / a[4]
#         rs = rs % a[4]
#         break
#
#     while (rs > a[5]):
#         g = rs / a[5]
#         rs = rs % a[5]
#         break
#
#     count = math.floor(b + d + e + f + g + c)
#
#     print(count)

t=int(input())
for _ in range(t):
    lis=[100,50,10,5,2,1]
    n=int(input())
    cnt=0
    for k in lis:
        if n%k==0:
            cnt=cnt+(n//k)
            break
        else:
            cnt=cnt+(n//k)
            n=n%k
    print(int(cnt))