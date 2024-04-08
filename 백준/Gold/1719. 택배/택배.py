import sys

from heapq import heappop, heappush

from math import inf

input = sys.stdin.readline

n,m = map(int,input().split())

g = {}

for i in range(n):

    g[i]=[]

for _ in range(m):

    a, b, c = map(int,input().split())

    g[a-1].append((c,b-1))

    g[b-1].append((c,a-1))

def dijk(start):

    pq = [(0,start)]

    dist = [inf for _ in range(n)]

    p_node = ["-"]*n

    dist[start] = 0

    while pq:

        w,v = heappop(pq)

        if dist[v] < w:

            continue

        for nw, nv in g[v]:

            if dist[nv] > w+nw:

                dist[nv] = w+nw

                p_node[nv] = v +1

                ans[nv][start] = v+1

                heappush(pq,(nw+w,nv))

    return

ans = [["-"]*n for _ in range(n)]

for i in range(n):

    dijk(i)

for i in range(n):

    print(*ans[i])