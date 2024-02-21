import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
# 1,1,에서(0, 0) n,m(n-1,m-1) 까지의 길

# , 서로 인접한 칸으로만 이동할 수 있다.


dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# 높이, 너비

maze = []
for _ in range(n):
    maze.append(list(input().rstrip()))

# visited = [[0 for _ in range(m)] for _ in range(m)]

q = deque([(0, 0, 1)])

while q:
    x, y, z = q.popleft()
    if x == n - 1 and y == m - 1:
        print(z)
        break
    if maze[x][y] == '1':
        maze[x][y] = '0'
        for dx, dy in dxy:
            if 0 <= x + dx < n and 0 <= y + dy < m:
                q.append((x + dx, y + dy, z + 1))

# print(maze)
