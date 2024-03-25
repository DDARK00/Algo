import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

lst = [list(input().strip()) for _ in range(n)]
# 맵 작성

# bfs

visit = [[0] * m for _ in range(n)]

next_q = [(x1 - 1, y1 - 1, 0)]
visit[x1-1][y1-1] = 1
find = False
# print(lst)
while not find:
    q = deque([])  # 좌표, 이동횟수
    q.extend(next_q)
    next_q = []

    while q:
        x, y, c = q.popleft()
        # print(x, y, lst[x][y])
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                visit[nx][ny] = 1

                if lst[nx][ny] == '0':
                    q.append((nx, ny, c))
                elif lst[nx][ny] == "#":
                    find = True
                    print(c+1)
                    break
                else:  # 1이면
                    next_q.append((nx, ny, c + 1))  # 다 털기
