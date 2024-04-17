import sys
from math import inf
from heapq import heappop, heappush

input = sys.stdin.readline
n, m = map(int, input().split())

# n개의 컴퓨터, m개의 회선
# 1번 컴퓨터는 보안 시스템을 설치할 슈퍼컴퓨터이다.
pq = [(0, 1)]  # w, v

g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    # 양방향
    g[a].append((c, b))  # w, v
    g[b].append((c, a))  # w, v

# dijk
cost = [[inf, 0] for _ in range(1 + n)]
cost[1][0] = 0
while pq:
    w, v = heappop(pq)

    if cost[v][0] < w:
        continue

    for nw, nv in g[v]:
        if cost[nv][0] > nw + w:
            cost[nv][0] = nw + w
            cost[nv][1] = v
            heappush(pq, (nw + w, nv))
print(n-1)

way = []
for i in range(2, n + 1):
    print(i,cost[i][1])

# 중복 간선은 없는건가???
