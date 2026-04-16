import sys
input=sys.stdin.readline
r,c=map(int,input().split())
n=int(input())
lst=list(sorted(map(int,input().split())))

target=[0]*n
ans=0
for i in range(n):
    if lst[i]>target[ans%c]:
        target[ans%c]=lst[i]
        ans+=1
print(min(ans,r*c))