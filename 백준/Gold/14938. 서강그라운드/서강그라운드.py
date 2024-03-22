import sys
from math import inf
from heapq import heappop, heappush

input = sys.stdin.readline

n, m, r = map(int, input().split())  # 지역의 수, 수색범위, 길의 개수

item_cnt = [*map(int, input().split())]

# edge

g = [[] for _ in range(n)]

for _ in range(r):  # edge
    a, b, c = map(int, input().split())
    g[a - 1].append((c, b - 1))
    g[b - 1].append((c, a - 1))
    # weight vertex

max_item = -1
for idx, item in enumerate(g):
    distance = [inf] * n
    distance[idx] = 0

    item_chk = [0] * n
    pq = [(0, idx)]  # weight, vertex
    get_item = item_cnt[idx]
    item_chk[idx] = 1

    while pq:
        w, v = heappop(pq)
        if distance[v] < w:
            continue

        for nw, nv in g[v]:  # idx 연결리스트
            # print(nw,nv,m,w)
            if nw + w <= m and distance[nv] >= nw + w:
                if not item_chk[nv]:
                    get_item += item_cnt[nv]
                    item_chk[nv] = 1
                distance[nv] = nw + w
                heappush(pq, (nw + w, nv))

    # print(idx, " : ", get_item)
    max_item = max(max_item, get_item)
print(max_item)
