import sys
from heapq import heappop, heappush

input = sys.stdin.readline

while True:
    m, n = map(int, input().split())
    # 집의 수, 길의 수

    if m == 0 and n == 0:
        break

    edges = [[] for _ in range(m)]
    all_cost = 0
    for _ in range(n):
        s, e, w = map(int, input().split())
        all_cost += w
        edges[s].append((w, e))
        edges[e].append((w, s))

    visited = [0] * m

    # visited[0] = 1
    pq = [(0, 0)]  # w,v

    # MST
    cost = 0
    while pq:
        w, v = heappop(pq)

        if not visited[v]:
            cost += w
            visited[v] = 1

            for x in edges[v]:
                if not visited[x[1]]:
                    heappush(pq, x)

    print(all_cost - cost)
