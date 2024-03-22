import sys
from collections import deque

input = sys.stdin.readline

n = int(input())  # n*n

# 0,0 -> n-1, n-1

q = deque([(0, 0, 0,)])  # x,y, count

lst = [input().strip() for _ in range(n)]  # 미로

visited = [[2501] * n for _ in range(n)]  # 방문 배열 -> 몇 번 부수고 도달했는지
visited[0][0] = 0
while q:
    x, y, c = q.popleft()
    if x == n - 1 and y == n - 1:
        print(c)
        break
    # 0은 검은 방, 1은 흰 방을 나타낸다.
    for dx, dy in [(1, 0), (-1, 0,), (0, 1), (0, -1)]:
        if 0 <= x + dx < n and 0 <= y + dy < n:  # 다음에 갈 곳
            # print(x + dx, y + dy)
            if lst[x + dx][y + dy] == '1' and visited[x + dx][y + dy] > c:
                visited[x + dx][y + dy] = c
                q.appendleft((x + dx, y + dy, c))
            elif lst[x + dx][y + dy] == '0' and visited[x + dx][y + dy] > c + 1:
                visited[x + dx][y + dy] = c + 1
                q.append((x + dx, y + dy, c + 1))
