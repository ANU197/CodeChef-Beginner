"""
The citizens of Byteland regularly play a game. They have blocks each denoting some integer from 0 to 9. These are arranged together in a random manner without seeing to form different numbers keeping in mind that the first block is never a 0. Once they form a number they read in the reverse order to check if the number and its reverse is the same. If both are same then the player wins. We call such numbers palindrome

Ash happens to see this game and wants to simulate the same in the computer. As the first step he wants to take an input from the user and check if the number is palindrome and declare if the user wins or not

Input
The first line of the input contains T, the number of test cases. This is followed by T lines containing an integer N.

Output
For each input output "wins" if the number is a palindrome and "losses" if not.

Constraints
1<=T<=20
1<=N<=10000
Input:
3
331
666
343

Output:
losses
wins
wins

"""


# for i in range(int(input())):
#     def reverse(n):
#         rev = 0
#         l = len(n)
#         for i in range(l):
#             rev = rev * 10 + int(n[l - 1 - i])
#
#         return rev
#
#
#     n = input()
#     result = int(reverse(n))
#
#     pre = int(n)
#
#     if (pre == result):
#         print("wins")
#     else:
#         print("looses")


for _ in range(int(input())):
    nums = input()
    a = nums
    b = nums[::-1]
    if a==b:
        print("wins")
    else:
        print("losses")