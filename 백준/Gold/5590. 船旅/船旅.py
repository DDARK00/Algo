import sys
from math import inf
from collections import defaultdict
from heapq import heappop, heappush

input = sys.stdin.readline
n, k = map(int, input().split())
# 섬 수, 입력 수

g = defaultdict(list)


def dijk(s, e):
    visited = [inf] * (n + 1)
    visited[s] = 0

    pq = [(0, s)]  # w, v

    while pq:
        w, v = heappop(pq)

        if visited[v] < w:
            continue

        for nw, nv in g[v]:
            if w + nw < visited[nv]:
                heappush(pq, (w + nw, nv))
                visited[nv] = w + nw

    if visited[e] == inf:
        return -1
    else:
        return visited[e]


for _ in range(k):
    lst = list(map(int, input().split()))
    if lst[0] == 1:
        # 노선  추가
        a, b, w = lst[1], lst[2], lst[3]

        g[a].append((w, b))
        g[b].append((w, a))
    else:
        # 출력
        print(dijk(lst[1], lst[2]))
        # 1에서 2로 가는 최소비용
        # 아주 기본적인 다익스트라