#Question link : https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem

#Answer:
def fib(x):
    a = 1
    b = 2
    for i in range(0,x):
        a,b = b,a+b
        if(b <= x):
            if(b%2 == 0):
                yield b
        else:
            break
         


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sums = 2
    for i in fib(n):
        sums += i
    print(sums)
