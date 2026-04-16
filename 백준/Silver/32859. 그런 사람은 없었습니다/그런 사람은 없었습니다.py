import sys
input=sys.stdin.readline
n, m=map(int,input().split())
s=int(input())

ok=0
money=[-1]*(n+1)
form=[-1]*(n+1)
for _ in range(m):
    i, t=map(int,input().split())
    if t==1: # 입급
        money[i]=ok
    else: # 폼
        form[i]=ok
        ok+=1

flag=True
for i in range(1,n+1):
    if money[i]==-1:
        continue
    if form[i]==-1:
        form[i]=ok
    if form[i]-money[i]>=s:
        print(i)
        flag=False

if flag:
    print(-1)