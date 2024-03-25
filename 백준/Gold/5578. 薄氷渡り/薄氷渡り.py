import sys

input = sys.stdin.readline

m = int(input())  # 가로
n = int(input())  # 세로

lst = [input().split() for _ in range(n)]

# print(lst)

visited = [[0 for _ in range(m)] for _ in range(n)]


def dfs(x, y, c):
    global m_c
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if 0 <= x + dx < n and 0 <= y + dy < m and lst[x + dx][y + dy] == "1" and not visited[x + dx][y + dy]:
            visited[x + dx][y + dy] = 1
            dfs(x + dx, y + dy, c + 1)
            m_c = max(m_c, c + 1)
            visited[x + dx][y + dy] = 0


# 1≤m≤90, 1≤n≤90인데 되나

m_c = 0
for i in range(n):
    for j in range(m):  # 모든 칸에 대하여
        if lst[i][j] == "1":  # 1이면 시작할 수 있음
            visited[i][j] = 1  # 최대 깊이
            dfs(i, j, 1)
            visited[i][j] = 0

print(m_c)
