import sys
input=sys.stdin.readline

p, n=map(int,input().split())
lst=list(map(int,input().split()))
lst.sort(reverse=True)
while p<200 and lst:
    p+=lst[-1]
    lst.pop()

print(n-len(lst))