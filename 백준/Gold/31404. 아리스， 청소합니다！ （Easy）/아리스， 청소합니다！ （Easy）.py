import sys
from collections import deque
input=sys.stdin.readline

h, w = map(int, input().split())
r, c, d = map(int, input().split())
rule = [[list(map(int,list(input().rstrip()))) for _ in range(h)]for _ in range(2)]

visited=1
dust = [[0]*w for _ in range(h)]
# 0 1 2 3
delta = [(-1,0),(0,1),(1,0),(0,-1)]
move=0
q=deque([(r,c)])

loop_cnt=h*w*4
while q:
    x, y = q.popleft()
    if dust[x][y]==0:
        use=0
        move+=visited
        visited=0
        dust[x][y]=1
    elif dust[x][y]==1:
        use=1
        if visited==loop_cnt:
            break
    visited+=1
    d = (d+rule[use][x][y])%4
    nx, ny = x+delta[d][0], y+delta[d][1]
    if 0<=nx<h and 0<=ny<w:
        q.append((nx, ny))
    else:
        break
# print(*visited, sep='\n')
print(move)