import sys
from collections import deque
input=sys.stdin.readline

h,w=map(int,input().split())
lst=[input().rstrip() for _ in range(h)]
visited=[[float('inf') for _ in range(w)]for _ in range(h)]

for i in range(h):
    for j in range(w):
        if lst[i][j]=='K':
            sx,sy=i,j
            break

visited[sx][sy]=0
dq=deque([(sx,sy,0)])

while dq:
    r,c,f=dq.popleft()
    if visited[r][c]<f:
        continue

    if lst[r][c]=='*':
        print(f)
        exit()

    for nr, nc in [(r-1, c+1), (r, c+1), (r+1, c+1)]:
        if 0<=nr<h and 0<=nc<w and lst[nr][nc]!='#' and visited[nr][nc]>f:
            visited[nr][nc]=f
            dq.appendleft((nr,nc,f))

    for dx, dy in [(1,0),(-1,0),(-1,-1),(0,-1),(1,-1)]:
        nr, nc=r+dx, c+dy
        if 0<=nr<h and 0<=nc<w and lst[nr][nc]!='#' and visited[nr][nc]>f+1:
            visited[nr][nc]=f+1
            dq.append((nr,nc,f+1))

print(-1)