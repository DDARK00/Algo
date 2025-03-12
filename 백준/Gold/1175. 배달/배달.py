import sys
from collections import deque
input=sys.stdin.readline

n, m = map(int, input().split())
cls = [list(input().rstrip()) for _ in range(n)]

val = 1

for i in range(n):
    for j in range(m):
        if cls[i][j]=="S":
            sx,sy = i, j
        elif cls[i][j]=="C":
            cls[i][j]=val
            val = 2

visited = [[[[0]*3 for _ in range(4)] for _ in range(m)] for _ in range(n)]
delta = [
    [(1,0,1),(-1,0,2),(0,-1,3)],
    [(0,1,0),(-1,0,2),(0,-1,3)],
    [(0,1,0),(1,0,1),(0,-1,3)],
    [(0,1,0),(1,0,1),(-1,0,2)],
    [(0,1,0),(1,0,1),(-1,0,2),(0,-1,3)]
]
# 0 1 2 3

q = deque([(sx, sy, 4, 0, 0)]) # x y d cnt val

while q:
    x, y, d, cnt, val = q.popleft()
    for dx, dy, nd in delta[d]:
        nx, ny = x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny][nd][val] and cls[nx][ny] != "#":
            nv = val
            visited[nx][ny][nd][val] = 1
            if cls[nx][ny] in [1, 2]:
                
                if nv + cls[nx][ny] == 3:
                    print(cnt+1)
                    exit()
                nv = cls[nx][ny]
            q.append((nx,ny,nd,cnt+1,nv))
print(-1)