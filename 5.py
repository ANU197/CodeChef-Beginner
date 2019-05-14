"""
Write a program to find the remainder when two given numbers are divided.
The first line contains an integer T, total number of test cases. Then follow T lines, each line contains two Integers A and B.
Find remainder when A is divided by B.

1 ≤ T ≤ 1000
1 ≤ A,B ≤ 10000


"""

T = int(input())
for i in range(T):
    a = input().split(" ")
    b = int(a[0])%int(a[1])
    print(b)
