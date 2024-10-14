import sys
from math import inf
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
lst = [input().rstrip() for _ in range(n)]

q = deque([(0,0,0,1)]) # x, y, k, cnt

visited = [[[inf]*(k+1) for _ in range(m)] for _ in range(n)]
for i in range(k):
    visited[0][0][k] = 1

while q:
    x, y, w, c = q.popleft()

    for dx, dy in [(0,1),(1,0),(-1,0), (0,-1)]:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m:
            if lst[nx][ny] == "1" and w<k and visited[nx][ny][w+1]>c+1:
                q.append((nx,ny,w+1,c+1))
                visited[nx][ny][w+1]=c+1
            elif lst[nx][ny] == "0" and visited[nx][ny][w]>c+1:
                q.append((nx,ny,w,c+1))
                visited[nx][ny][w]=c+1
ans = min(visited[n-1][m-1])
print(-1 if ans == inf else ans)        