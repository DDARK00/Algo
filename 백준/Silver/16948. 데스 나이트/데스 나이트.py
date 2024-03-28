# (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)로 이동할 수 있다.

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())  # 체스판의 크기

r1, c1, r2, c2 = map(int, input().split())


# 1 -> 2


# bfs
def bfs(r, c):
    q = deque([(r1, c1, 0)])  # 칸, 이동횟수
    visited = [[0] * n for _ in range(n)]  # 맵

    visited[r][c] = 1
    while q:
        r, c, cnt = q.popleft()  #

        if r == r2 and c == c2:
            return cnt

        for dx, dy in [(- 2, - 1), (- 2, 1), (0, - 2), (0, + 2), (2, - 1), (2, 1)]:
            if 0 <= r + dx < n and 0 <= c + dy < n and not visited[r + dx][c + dy]:
                q.append((r + dx, c + dy, cnt + 1))
                visited[r + dx][c + dy] = 1
    else:
        return -1


print(bfs(r1, c1))
