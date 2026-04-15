import sys
input=sys.stdin.readline

n=int(input())
ans=0
p=0
for k in map(int,input().split()):
    ans=max(ans,k-p)
    p+=k
print(ans)