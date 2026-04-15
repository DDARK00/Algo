import sys
input=sys.stdin.readline
input()

mn=10e9
ans=0

for i in map(int,input().split()):
    mn=min(mn,i)
    ans=max(ans,i-mn)
    print(ans,end=" ")