import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
# 세로 가로

lst = [input().strip() for _ in range(n)]
# 맵

visited = [[200 for _ in range(m)] for _ in range(n)]

# 현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동
# 0,0 -> n-1, m-1

# bfs

q = deque([(0, 0, 0)])  # x, y, cnt
visited[0][0] = 0
# x y 좌표에 벽을 몇 번 부수고 도달할 수 있는가
while q:
    x, y, c = q.popleft()
    if x == n - 1 and y == m - 1:
        print(c)
        break
    if visited[x][y] < c:
        continue

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if 0 <= x + dx < n and 0 <= y + dy < m:
            if lst[x + dx][y + dy] == "1" and visited[x + dx][y + dy] > c + 1:
                q.append((x + dx, y + dy, c + 1))
                visited[x + dx][y + dy] = c + 1

            elif lst[x + dx][y + dy] == "0" and visited[x + dx][y + dy] > c:
                q.appendleft((x + dx, y + dy, c))
                visited[x + dx][y + dy] = c