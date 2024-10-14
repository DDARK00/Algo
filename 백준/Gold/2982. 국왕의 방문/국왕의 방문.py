import sys
from heapq import heappop, heappush
from collections import defaultdict
from math import inf
input=sys.stdin.readline

n, m = map(int, input().split())
a, b, k, g = map(int, input().split())
# s e
go = list(map(int, input().split()))

gr = defaultdict(list)
gor = defaultdict(dict)
for _ in range(m):
    x, y, w = map(int, input().split())
    gr[x].append((w, y)) 
    gr[y].append((w, x))
    gor[x][y] = w
    gor[y][x] = w

def dijk(start, end):
    visited = [inf]*(n+1)
    visited[start] = k

    pq = [(k, start)]
    while pq:
        w, v  = heappop(pq)
        if visited[v]<w:
            continue

        for nw, nv in gr[v]:
            if delay[nv].get(v):
                go_start, go_end = delay[nv][v]
                # print(go_start, go_end, "<-", v,nv,w,nw)
                if go_start<= w < go_end:
                    nw+= go_end-w
            if visited[nv]>w+nw:
                heappush(pq, (nw+w, nv))
                visited[nv] = nw+w
    # print(visited)
    return visited[end]
delay = defaultdict(dict)

wang = 0

for i in range(1, g):
    now = go[i]
    before = go[i-1]
    W = gor[now][before]
    delay[before][now] = (wang, wang+W)
    delay[now][before] = (wang, wang+W) # st ed 0<= target < weight
    wang += W
# print(delay)
    
print(dijk(a, b)-k)