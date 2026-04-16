import sys
input=sys.stdin.readline

n,d=map(int,input().split())
lst=list(map(int,input().split()))
k=max(lst)
t=max(0,k-d)
ans=0
for c in lst:
    ans+=max(0,c-t)
print(ans)