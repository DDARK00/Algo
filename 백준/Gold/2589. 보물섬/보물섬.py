import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
# 세로 가로

lst = [input().strip() for _ in range(n)]
# 지도

visited_out = [[0 for _ in range(m)] for _ in range(n)]
m_cnt = -1
# print(visited_out)
for i in range(n):
    for j in range(m):

        if lst[i][j] != "W" and not visited_out[i][j]:
            visited_out[i][j] = 1
            visited = [[0 for _ in range(m)] for _ in range(n)]
            c = 1
            q = deque([(i, j, c)])
            # print(i,j,"->>>>")
            visited[i][j] = 1
            while q:
                x, y, c = q.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= x + dx < n and 0 <= y + dy < m and lst[x + dx][y + dy] != "W":
                        if not visited[x + dx][y + dy]:
                            visited[x + dx][y + dy] = c + 1
                            q.append((x + dx, y + dy, c + 1))
            else:
                # print(visited)
                m_cnt = max(c - 1, m_cnt)
print(m_cnt)
