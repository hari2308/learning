"""
Write a program to input a list of n integers in an array and arrange them in a way similar to the to-and-fro movement of a Pendulum.

The minimum element out of the list of integers, must come in center position of array. If there are even elements, then minimum element should be moved to (n-1)/2 index (considering that indexes start from 0)
The next number (next to minimum) in the ascending order, goes to the right, the next to next number goes to the left of minimum number and it continues like a Pendulum.
Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n denoting the size of the array. Then next line contains N space separated integers forming the array.

Output:
Output the array in Pendulum Arrangement.

Constraints:
1<=T<=500
1<=N<=100
1<=a[i]<=1000

Example:
Input:
2
5
1 3 2 5 4
5
11 12 31 14 5

Output:
5 3 1 2 4
31 12 5 11 14
"""




#code
def test(x, y):

    y = sorted(y)
    a =[]
    for i in range(0,x):
        if i%2 == 0:
            a.insert(0,y[i])
        else:
            a.insert(len(a), y[i])

    return " ".join([str(i) for i in a])   

for i in range(0, int(input().strip())):
    x = int(input().strip())
    y = list(map(int, input().split()))
    print(test(x,y))
