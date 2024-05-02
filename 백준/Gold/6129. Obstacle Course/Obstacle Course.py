import sys
from math import inf
from collections import deque

input = sys.stdin.readline

n = int(input())

lst = [input().rstrip() for _ in range(n)]

for i in range(n):
    for j in range(n):
        if lst[i][j] == "A":
            sx = i
            sy = j
        elif lst[i][j] == "B":
            ex = i
            ey = j

visited = [[[inf, inf, inf, inf] for _ in range(n)] for _ in range(n)]
#  (1 <= N <= 100)
# 0-1 bfs


q = deque([])
for d in range(4):  # 시작점에 4방향에서 왔다고 가정
    q.append((sx, sy, d, 0))
    visited[sx][sy][d] = 0

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while q:
    x, y, d, c = q.popleft()  # 좌표, 방향, 움직인 횟수
    for i in range(4):
        nx, ny = x + delta[i][0], y + delta[i][1]
        if 0 <= nx < n and 0 <= ny < n and lst[nx][ny] != 'x' and visited[nx][ny][i] > c:
            if d == i:
                visited[nx][ny][d] = c
                q.appendleft((nx, ny, d, c))
            else:
                q.append((nx, ny, i, c + 1))
                visited[nx][ny][i] = c + 1
print(min(visited[ex][ey]))
# print(visited)
