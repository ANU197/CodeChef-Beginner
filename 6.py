"""
You're given an integer N. Write a program to calculate the sum of all the digits of N.

Input
The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

Output
Calculate the sum of digits of N.

Constraints
1 ≤ T ≤ 1000
1 ≤ N ≤ 1000000

"""







t = int(input())
s = []

def sum(n):
    sum = 0
    for i in range(0, len(n)):
        sum += int(n[i])
    return sum

for i in range(t):
    n = input()
    s.append(sum(n))

print(*s, sep='\n')