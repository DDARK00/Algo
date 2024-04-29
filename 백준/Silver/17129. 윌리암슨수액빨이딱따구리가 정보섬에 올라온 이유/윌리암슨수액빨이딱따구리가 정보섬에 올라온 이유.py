import sys
from collections import deque

input = sys.stdin.readline

# 0빈복도 1장애물
# 2에서  3 4 5 중에 하나로 가는 최단거리

n, m = map(int, input().split())
# 900만 n 2n

lst = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if lst[i][j] == '2':
            sx = i
            sy = j
            lst[i][j] = '1'
            break

q = deque([(sx, sy, 0)])
while q:
    x, y, c = q.popleft()
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and lst[nx][ny] != '1':
            if lst[nx][ny] != '0':
                print('TAK')
                print(c + 1)
                exit()
            else:
                lst[nx][ny] = '1'
                q.append((nx, ny, c + 1))

print("NIE")
