import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

lst = [input().split() for _ in range(n)]
# 행성

visited = [[0] * m for _ in range(n)]

q = deque([])
ans = 0

for i in range(n):
    for j in range(m):

        # bfs
        if lst[i][j] == "0" and not visited[i][j]:
            ans += 1
            q.append((i, j))
            visited[i][j] = 1
            while q:
                x, y = q.popleft()

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx = (x + dx + n) % n
                    ny = (y + dy + m) % m
                    # print(nx, ny)
                    if lst[nx][ny] == "0" and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        q.append((nx, ny))

print(ans)
