import sys
from math import inf
from heapq import heappop, heappush
from collections import defaultdict
input=sys.stdin.readline

k, n = map(int, input().split())
g = defaultdict(list)

for _ in range(n):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

pq = [(0,1)] # w, v
time = [inf] * (k+1)
time[1] = 0

# 1 -> k
while pq:
    w, v = heappop(pq)
    if time[v]<w:
        continue
    for nv in g[v]:
        # w = spent
        diff = abs(nv-v)*5
        if v > nv : # down
            # print("down : ",v,"->",nv,diff)
            if w//diff %2 == 1: # odd
                if w%diff != 0:
                    nw = diff+diff-w%diff
                else:
                    nw=0
            else: # even
                nw = diff-w%diff

        else: # up
            # print("up : ",v,"->", nv, diff)
            if w//diff %2 == 0: # even
                if w%diff !=0:
                    nw = diff+diff-w%diff
                else:
                    nw=0
            else: # odd
                nw = diff - w%diff
        nw = nw + diff + w
        if time[nv]>nw:
            # print("in : ", nv,"->", nw,diff,w)
            heappush(pq, (nw, nv))
            time[nv] = nw

print(time[k])