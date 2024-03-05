import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

# RGB
# RG / B

lst = [input().strip() for _ in range(n)]

# bfs
q = deque([])

# 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)

# 100*100 10000 1초?

yes = 0
no = 0
visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            q.append((i, j))
            yes += 1
            # 색약아님, 같은색 판별
            visited[i][j] = 1
            target = lst[i][j]

            # bfs
            while q:
                x, y = q.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= dx + x < n and 0 <= dy + y < n:
                        if not visited[dx + x][dy + y] and lst[dx + x][dy + y] == target:
                            visited[dx + x][dy + y] = 1
                            q.append((dx + x, dy + y))

print(yes, end=" ")
# 색약
# RG / B
for i in range(n):
    lst[i] = lst[i].replace("G", "R")

for i in range(n):
    for j in range(n):
        if visited[i][j]:
            q.append((i, j))
            no += 1

            visited[i][j] = 0
            target = lst[i][j]
            # R==G
            # B

            # bfs
            while q:
                x, y = q.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= dx + x < n and 0 <= dy + y < n:
                        if visited[dx + x][dy + y] and lst[dx + x][dy + y] == target:
                            visited[dx + x][dy + y] = 0
                            q.append((dx + x, dy + y))

print(no)
'''
RRB
BRR
RBR

3
RGB
BGR
GBR

'''
