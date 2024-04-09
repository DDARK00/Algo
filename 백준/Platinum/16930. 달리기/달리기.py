import sys
from collections import deque
input = sys.stdin.readline
n, m, k = map(int, input().split())
lst = [input().rstrip() for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split())
visited =[[600001]*m for _ in range(n)]
q = deque([(x1 - 1, y1 - 1)])
visited[x1 - 1][y1 - 1] = 0

x2 -= 1
y2 -= 1

while q:
    x, y = q.popleft()
    if x == x2 and y == y2:
        print(visited[x][y])
        exit()
        break

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        for i in range(1, k + 1):
            nx = x + dx * i
            ny = y + dy * i
            if 0 <= nx < n and 0 <= ny < m and lst[nx][ny] != "#" :
                if visited[nx][ny] ==600001:
                    visited[nx][ny]= visited[x][y]+1
                    q.append((nx, ny))
                elif visited[nx][ny] <= visited[x][y] :
                    break
                    # 이미 탐색한 방향에 대해서 break
            else:
                break

print(-1)

# 더 이상은 Naver...
# 여기까지 정리하고 더 뭐 못 하겠다...ㅕ 하... 포기...