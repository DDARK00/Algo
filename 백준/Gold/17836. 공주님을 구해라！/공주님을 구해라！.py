import sys
from collections import deque

input = sys.stdin.readline

n, m, t = map(int, input().split())
# 높이, 너비, 제한시간


lst = [input().strip().split() for _ in range(n)]

# 0, 0 에서 n-1, m-1 로 가야 한다

q = deque([(0, 0, 0)])
# x, y, cnt
visited = [[0 for _ in range(m)] for _ in range(n)]
# bfs

dist = 10001
find = False
while q:
    # 루트는 2개
    # 1. 그람 찾고 벽뚫기
    # 2. 스트레이트로 구하러 가기
    # bfs니까 그람보다 공주를 먼저 찾으면 break
    x, y, cnt = q.popleft()
    if cnt > t:
        continue

    if lst[x][y] == "2":
        left_dist = abs(n - 1 - x) + abs(m - 1 - y)
        if cnt + left_dist <= t:
            dist = min(dist, cnt + left_dist)
            find = True
        # gram
    elif x == n - 1 and y == m - 1:
        find = True
        dist = min(cnt, dist)
        # 공주
        break

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        # print(dx+x,dy+y)
        if 0 <= x + dx < n and 0 <= y + dy < m and lst[x + dx][y + dy] != "1" and not visited[x + dx][y + dy]:
            visited[x + dx][y + dy] = 1

            q.append((x + dx, y + dy, cnt + 1))
# print(dist)
# print(lst)
# print(visited)
if find:
    print(dist)
else:
    print("Fail")