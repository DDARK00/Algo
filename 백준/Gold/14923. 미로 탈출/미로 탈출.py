import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
hx, hy = map(int, input().split())
ex, ey = map(int, input().split())

hx -= 1
hy -= 1  # 시작
ex -= 1
ey -= 1  # 끝

lst = [input().split() for _ in range(n)]

q = deque([(hx, hy, 0, 1)])  # 좌표, 움직인 횟수, 벽 뚫었니?

visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
# print(visited)
visited[hx][hy][0] = 1
find = False
cnt = -1
while q:
    x, y, c, d = q.popleft()
    if x == ex and y == ey:
        find = True
        cnt = c
        break
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if lst[nx][ny] == "0":
                if d and not visited[nx][ny][0]:
                    visited[nx][ny][0] = 1

                    q.append((nx, ny, c + 1, 1))

                elif not d and not visited[nx][ny][1]:
                    q.append((nx, ny, c + 1, 0))
                    visited[nx][ny][1] = 1

            elif lst[nx][ny] == "1" and d == 1 and not visited[nx][ny][1]:  # 1이 use
                visited[nx][ny][1] = 1

                q.append((nx, ny, c + 1, 0))

    #
    #
    # if find:
    #     break
print(cnt)
# print(visited)
'''

5 6
1 1
5 6
0 1 1 1 0 0
0 1 1 0 0 0
0 1 0 0 1 0
0 1 0 0 1 0
0 1 0 0 0 0

5 2
1 1
5 1
0 0
1 0
0 0
1 1
0 1
'''
