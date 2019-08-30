#Question : Project Euler #3: Largest prime factor
#link : https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem

def prime(x):
    for i in range(3,x//2+1,2):
        if (x%i) == 0:
            return False
    else:
        return True
        


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for i in range(n//2, 2, -1):
        if n%i == 0 and prime(i):
            print(i)
            break
    else:
        print(n)
        
#four test cases passed and two 2 cases failed due to Terminated due to timeout :(

