import sys
from collections import deque

input = sys.stdin.readline
# .빈곳 *물 X돌

# D굴 S고슴도치
r, c = map(int, input().split())

lst = [list(input().strip()) for _ in range(r)]

water = []
biber = []
visited = [[0] * c for _ in range(r)]
visited_water = [[0] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if lst[i][j] == "*":
            water.append((i, j))
            visited[i][j] = 1
            visited_water[i][j] = 1

        elif lst[i][j] == "X":
            visited[i][j] = 1
            visited_water[i][j] = 1

        elif lst[i][j] == "S":
            visited[i][j] = 1
            biber.append((i, j))
# 어차피 물 있는데는 못 가니까 싹 방문처리

bq = deque(biber)
wq = deque(water)


def find():
    cnt = 0

    while True:
        next_B = []
        next_W = []
        cnt += 1
        while wq:
            x, y = wq.popleft()
            for dx, dy in [(1, 0), (0, 1), (-1, 0,), (0, -1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < r and 0 <= ny < c and not visited_water[nx][ny]:
                    if lst[nx][ny] == "D":
                        continue

                    visited[nx][ny] = 1
                    visited_water[nx][ny] = 1
                    next_W.append((nx, ny))

        while bq:
            x, y = bq.popleft()
            for dx, dy in [(1, 0), (0, 1), (-1, 0,), (0, -1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                    if lst[nx][ny] == "D":
                        return cnt
                    visited[nx][ny] = 1
                    next_B.append((nx, ny))


        if not next_B:
            break
        else:
            bq.extend(next_B)
            wq.extend(next_W)

    return "KAKTUS"


print(find())