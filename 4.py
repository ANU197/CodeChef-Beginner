"""
The purpose of this problem is to verify whether the method you are using to read input data is sufficiently
fast to handle problems branded with the enormous Input/Output warning.
You are expected to be able to process at least 2.5MB of input data per second at runtime.

The input begins with two positive integers n k (n, k<=107). The next n lines of input contain one positive integer ti, not greater than 109, each.

OUTPUT = Write a single integer to output, denoting how many integers ti are divisible by k.


"""

n = input().split(" ")
b = 0
for i in range(int(n[0])):
    a = int(input())
    if(a%int(n[1])==0):
        b=b+1



print(b)