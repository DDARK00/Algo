import sys
from math import inf
from collections import defaultdict
from heapq import heappop,heappush
input=sys.stdin.readline

n,m,k = map(int, input().split())

g = defaultdict(list)
for _ in range(m):
    u, v, c = map(int, input().split())
    # g[u].append((v, c))
    g[v].append((u, c))
    # vertex, weight

pq = []
dist = [inf]*(n+1)
for num in map(int, input().split()):
    pq.append((0, num))
    dist[num] = 0

while pq:
    w, v = heappop(pq)
    if dist[v]<w:
        continue

    for nv, nw in g[v]:
        if dist[nv]>nw+w:
            heappush(pq, (nw+w, nv))
            dist[nv] = nw+w


ans = [0,-1]
for i in range(1,n+1):
    if dist[i]>ans[1]:
        ans = [i,dist[i]]
print(*ans, sep='\n')