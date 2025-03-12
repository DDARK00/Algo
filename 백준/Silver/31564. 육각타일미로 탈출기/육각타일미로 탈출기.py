import sys
from collections import deque
input=sys.stdin.readline
n,m,k = map(int, input().split())

visited = [[0]*m for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    visited[a][b]=1
visited[0][0]=1
q = deque([(0,0,0)])

while q:
    x, y, c = q.popleft()
    r = 1 if x%2 else -1
    for dx, dy in [(0,-1),(0,1),(-1,0),(-1,r),(1,0),(1,r)]:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            if nx == n-1 and ny == m-1:
                print(c+1)
                exit()
            visited[nx][ny] = 1
            q.append((nx, ny, c+1))

print(-1)