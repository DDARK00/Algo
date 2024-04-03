import sys
# import copy
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
# 연구소의 크기, 바이러스의 개수

lst = [input().split() for _ in range(n)]
# 연구소
# 0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 칸


ca = []
all_box = n * n
for i in range(n):
    for j in range(n):
        if lst[i][j] == "2":
            ca.append((i, j))
            lst[i][j] = "0"
        elif lst[i][j] == "1":
            all_box -= 1


def dfs(k, l):
    global min_day
    if k == m:
        # bfs
        # print(select)
        # start = copy.deepcopy(select)
        q = deque([])
        # 50*50 10개 2중for문

        visited = [[0 for _ in range(n)] for _ in range(n)]
        day = 0
        v_cnt = 0
        for x, y in select:
            visited[x][y] = 1
            v_cnt += 1
            q.append((x, y))
            # 일단 첫 바이러스 위치 잡고

        while True:
            if day >= min_day:
                break
            # print(q)
            next_time = []

            while q:
                x, y = q.popleft()

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx = dx + x
                    ny = dy + y
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and lst[nx][ny] == "0":
                        visited[nx][ny] = 1
                        v_cnt += 1

                        next_time.append((nx, ny))
            if next_time:
                q.extend(next_time)
                day += 1

            else:
                if v_cnt == all_box:
                    min_day = min(min_day, day)
                break
        # print( v_cnt, all_box)
        return

    for i in range(l, len(ca)):
        select.append(ca[i])
        dfs(k + 1, i + 1)
        select.pop()


min_day = 2501

select = []

dfs(0, 0)
min_day = min_day if min_day != 2501 else -1
print(min_day)
'''
5 5
2 2 2 2 2
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
'''
