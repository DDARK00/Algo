import sys
from collections import defaultdict
from math import inf
from heapq import heappop, heappush

input = sys.stdin.readline

n, e, p = map(int,input().split())

g = defaultdict(list)

for _ in range(e):
    a, b, c = map(int,input().split())
    g[a].append((c, b)) # w, v
    g[b].append((c, a))

def dijk(start):
    pq = [(0, start)]
    visited = [inf] * (n+1)
    visited[start] = 0
    # w, v
    while pq:
        w, v = heappop(pq)
        if visited[v]<w:
            continue

        for nw, nv in g[v]:
            if visited[nv]>nw+w:
                visited[nv] = nw+w
                heappush(pq,(nw+w,nv))
    return visited
first = dijk(1)
second = dijk(p)
if first[n] == second[1]+second[n]:
    print('SAVE HIM')
else:
    print('GOOD BYE')
# 1->n == 1->p->n SAVE HIM / GOOD BYE