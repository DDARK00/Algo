import sys

from collections import deque

input = sys.stdin.readline

badak = []
n, m = map(int, input().split())

for _ in range(n):
    badak.append(list(input()))

q = deque([])
cnt = 0
for i in range(n):
    for j in range(m):
        if badak[i][j] == "-":
            cnt += 1
            q.append((i, j))
            badak[i][j] = "x"
            while q:
                x, y = q.popleft()
                # 가로로만 움직임
                if y - 1 >= 0 and badak[i][y - 1] == "-":
                    badak[i][y - 1] = "x"
                    q.append((i, y - 1))
                elif y + 1 < m and badak[i][y + 1] == "-":
                    badak[i][y + 1] = "x"
                    q.append((i, y + 1))

        elif badak[i][j] == "|":
            cnt += 1
            q.append((i, j))
            badak[i][j] = "x"
            while q:
                x, y = q.popleft()
                # 세ㅗ로로만 움직임
                if x - 1 >= 0 and badak[x - 1][j] == "|":
                    badak[x - 1][j] = "x"
                    q.append((x - 1, j))
                elif x + 1 < n and badak[x + 1][j] == "|":
                    badak[x + 1][j] = "x"
                    q.append((x + 1, j))
print(cnt)
