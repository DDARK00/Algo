import sys
input=sys.stdin.readline

for _ in range(int(input())):
    cmd=input().rstrip()

    xl,xr,yl,yr=0,0,0,0
    x,y,d=0,0,0 # 북동남서
    delta=[(1,0),(0,1),(-1,0),(0,-1)]

    for c in cmd:
        if c=='L':
            d=(d+4-1)%4
        elif c=='R':
            d=(d+1)%4
        else: # F B
            nd=d if c=='F' else (d+2)%4
            dx,dy=delta[nd]
            x+=dx
            y+=dy
            xl=min(xl,x)
            xr=max(xr,x)
            yl=min(yl,y)
            yr=max(yr,y)
    print((xr-xl)*(yr-yl))