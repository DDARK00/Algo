import sys
input=sys.stdin.readline
n = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())
for i in range(ax):
    a2b = i
    a2c = ax-i
    b2c = cy-a2c
    if b2c<0 :
        continue
    b2a = bx-b2c
    if b2a <0 :
        continue
    c2a = ay-b2a
    if c2a<0 :
        continue
    c2b = cx-c2a
    if c2b<0:
        continue
    print(1)
    print(a2b,a2c)
    print(b2a,b2c)
    print(c2a,c2b)
    exit()
print(0)