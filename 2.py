"""""
Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction if X is a multiple of 5,
and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges). For each successful withdrawal the bank charges 0.50 $US.
 Calculate Pooja's account balance after an attempted transaction.

 Positive integer 0 < X <= 2000 - the amount of cash which Pooja wishes to withdraw.

Nonnegative number 0<= Y <= 2000 with two digits of precision - Pooja's initial account balance.

# output
Example - Successful Transaction
Input:
30 120.00

Output:
89.50
Example - Incorrect Withdrawal Amount (not multiple of 5)
Input:
42 120.00

Output:
120.00
Example - Insufficient Funds
Input:
300 120.00
200
Output:
120.00
"""

a = input().split(" ")
x = float(a[0])
y = float(a[1])
if(x>y):
    print("Insufficient Funds")
elif(x<y):
    if(x%5==0):
        print("Successful Transaction")
        print(y-x-0.5)
    else:
        print("Incorrect Withdrawal Amount(not multiple of 5)")
