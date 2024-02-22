import sys
import copy
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
# n*n짜리 지도에 m개만 남김
# 1은 집 2는 치킨집
'''
def bfs(start):
    global super_min_m
    q = deque(start)
    msum = 0
    visited = copy.deepcopy(lst)
    while q:
        x, y, c = q.popleft()
        # print(x,y)
        # xy좌표, cnt
        # print(visited)
        if msum >super_min_m:
            msum = 3250001
            break
        for dx, dy in dxy:
            if 0 <= x + dx < n and 0 <= y + dy < n:
                if visited[x + dx][y + dy] == '0' or visited[x + dx][y + dy] == '2':

                    q.append((x + dx, y + dy, c + 1))
                    # visited[x + dx][y + dy] = c + 1
                elif visited[x + dx][y + dy] == '1':
                    # print(c)
                    msum += c + 1
                    q.append((x + dx, y + dy, c + 1))
                visited[x + dx][y + dy] = c + 1

    # print(msum)
    super_min_m = min(super_min_m, msum)
    # print(visited)
'''

lst = []

for _ in range(n):
    lst.append(input().split())

home = []
chik = []

for i in range(n):
    for j in range(n):
        if lst[i][j] == "1":
            home.append((i, j))
        if lst[i][j] == "2":
            # chik.append((i, j, 0))
            chik.append((i, j))

# |집i - 칰i| + |집j + 칰j|
# 의 합을 구하는데, 구한 m들의 최소
# 50*50 2N 100 m13
# 2500 100 13
# 2500 + 1300 100 1300

selected = []

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def calcdis(chick):
    global super_min_m
    # 치킨집 리스트를 받아서-> 각 집에서-> 가까운 치킨집 거리 더하기
    sumdis = 0
    cnt = 0
    for hx, hy in home:
        distance = 3500001
        for cx, cy in chick:
            distance = min(abs(hx - cx) + abs(hy - cy), distance)
        sumdis += distance
        cnt += 1
        if sumdis > super_min_m:
            sumdis = 3500001
            break
    # print(sumdis)
    # print('연산횟수', cnt)
    super_min_m = min(sumdis, super_min_m)


def dfs(k):
    global super_min_m

    # chik개 중 m개
    if len(selected) == m:
        # print(selected)
        start = copy.deepcopy(selected)
        # bfs(start)
        calcdis(start)

    for i in range(k, len(chik)):

        if chik[i] not in selected:
            selected.append(chik[i])
            dfs(i)
            selected.pop()


# 모든 가능한 m개의 조합 중복제거
super_min_m = 3250001

dfs(0)
# 거리 계산은 어떻게 하냐...
print(super_min_m)

# print(lst)

## BFS로 시간 초과가 난 이유?
# 상수 계산이 훨 빠르다
# 아 열심히 돌렸는데 흑흑
# BFS는 완전탐색 + 경로탐색까지 추가돼서 그런가
# 생각해 보면 상수 덧셈뺄셈보다 손이 많이 갈 것 같긴 함 ㅇㅇㄹㅇ