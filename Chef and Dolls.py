"""
Chef is fan of pairs and he likes all things that come in pairs.
He even has a doll collection in which all dolls have paired.
One day while going through his collection he found that there are odd number of dolls.
Someone had stolen a doll!!!

Help chef find which type of doll is missing..

Input
The first line contains the number of test cases.
Second line of the input contains the number of elements in the array.
The next n lines are the types of each doll that is left.
Output
Find the type of doll that doesn't have a pair

Constraints
1<=T<=10
1<=N<=100000 (10^5)
1<=ti<=100000
Input:
1
3
1
2
1


Output:
2


Input:
1
5
1
1
2
2
3
Output:
3

"""






try:

    for _ in range(int(input())):
        a = []
        n = int(input())
        for j in range(n):
            a.append(int(input()))


    b = list(set(a))
    count = 0
    for i in range(len(b)):
        for j in range(len(a)):
            if b[i] == a[j]:
                count += 1
        if count % 2 == 1:
            print(b[i])
            break






except:
    pass
