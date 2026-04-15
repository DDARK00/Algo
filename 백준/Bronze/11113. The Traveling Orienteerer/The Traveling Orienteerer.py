import sys, math
input=sys.stdin.readline

n=int(input())
dot=[tuple(map(float,input().split())) for _ in range(n)]

m=int(input())
for _ in range(m):
    p=int(input())
    rt=list(map(int, input().split()))
    ans = 0
    for i in range(p-1):
        st=rt[i]
        ed=rt[i+1]
        sx, sy = dot[st]
        ex, ey = dot[ed]
        ans+=math.sqrt((sx-ex)**2 + (sy-ey)**2)
    print(round(ans))