import sys
input=sys.stdin.readline

sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
px, py = map(int, input().split())

if sx==ex and sy==ey:
    print(0)
    exit()

if sx == ex:
    if sx==px and min(sy,ey)<py<max(sy,ey):
        print(2)
    else:
        print(0)
elif sy == ey:
    if sy==py and min(sx,ex)<px<max(sx,ex):
        print(2)
    else:
        print(0)
else:
    print(1)