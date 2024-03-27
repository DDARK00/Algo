import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())  # 세로 가로 음식물 수

lst = [[0] * m for _ in range(n)]
# visited = [[0] * m for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    lst[a - 1][b - 1] = 1
    
m_cnt = 0
for i in range(n):
    for j in range(m):
        if lst[i][j]:
            q = deque([(i, j)])  # 좌표, 칸 수
            cnt = 1
            lst[i][j] = 0
            while q:
                x, y = q.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < n and 0 <= ny < m and lst[nx][ny]:
                        cnt += 1
                        lst[nx][ny] = 0
                        q.append((nx, ny))
            m_cnt = max(m_cnt, cnt)
print(m_cnt)
