import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

# m*n짜리 상자, 높이h
#  하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향

# h층의 n줄의 m번째

lst = []
for _ in range(h):
    temp_box = []
    for i in range(n):
        temp_box.append(input().split())
    lst.append(temp_box)

good_list = []
good_cnt = 0

punk = 0
# 토마토가 없는 부분

for i in range(h):
    for j in range(n):
        for l in range(m):
            if lst[i][j][l] == '1':
                good_list.append((i, j, l))
                good_cnt += 1
            elif lst[i][j][l] == '-1':
                punk += 1

# print(good_list)

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# bfs
q = deque(good_list)

# 전체 토마토의 개수 = n*m*h

visited = []
next_day = []
days = 0
while q:
    x, y, z = q.popleft()
    # x가h y가n z가m

    for i in range(6):
        # 여섯 방향
        new_x = x + dx[i]
        new_y = y + dy[i]
        new_z = z + dz[i]
        if 0 <= new_x < h and 0 <= new_y < n and 0 <= new_z < m:
            # 범위 내에 있다면
            if lst[new_x][new_y][new_z] == '0':
                lst[new_x][new_y][new_z] = '1'
                next_day.append((new_x, new_y, new_z))
                good_cnt += 1

    if not q:
        days += 1
        if next_day:
            q.extend(next_day)
            next_day = []
    # 하루 정산

# print(good_cnt, h * n * m, punk)
# print(days)
if h * n * m == (good_cnt + punk):
    # 퍼펙트 토마토
    print(days - 1)
else:
    # 다 돌리고도 부족할 때
    print(-1)
