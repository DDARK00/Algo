import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = map(int, input().split())
# n*n

visited = [[0]*(n+1) for _ in range(n+1)]
g = defaultdict(list)
for _ in range(m):
    x, y, a, b = map(int, input().split())
    g[(x, y)].append((a, b))

q = deque([(1,1)])
visited[1][1]=1
# 1 can go
# 2 gone
c = 1


while q:
    x, y = q.popleft()
    if visited[x][y] == 0:
        continue
    # print(x, y)
    visited[x][y] = 2
    for gx, gy in g[(x, y)]:
        if visited[gx][gy]==0:
            visited[gx][gy]=1
            # 새로 켜진곳이 있으면
            c+=1
            for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                nx, ny = gx+dx, gy+dy
                if 0<=nx<=n and 0<=ny<=n and visited[nx][ny] == 2:
                    q.appendleft((nx,ny))
                    break

    for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
        nx, ny = x+dx, y+dy
        if 0<=nx<=n and 0<=ny<=n and visited[nx][ny] != 2:
            if visited[nx][ny] == 1:
                q.appendleft((nx, ny))
            else:
                q.append((nx, ny))
print(c)