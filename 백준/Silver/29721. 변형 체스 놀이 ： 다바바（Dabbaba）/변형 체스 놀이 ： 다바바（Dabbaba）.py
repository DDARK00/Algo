import sys
input=sys.stdin.readline

n,k=map(int,input().split())
chk={}
for _ in range(k):
    x,y=map(int,input().split())
    chk[(x,y)]=1
ans={}
for x,y in chk:
    for dx,dy in [(2,0),(-2,0),(0,2),(0,-2)]:
        if 0<x+dx<=n and 0<y+dy<=n and not chk.get((x+dx,y+dy)):
            ans[(x+dx,y+dy)]=1
print(len(ans))