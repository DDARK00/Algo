import sys
input=sys.stdin.readline
n=int(input())
lst=[0]*(n+1)
for i in map(int,input().split()):
    lst[i]=lst[i-1]+1

print(n-max(lst))