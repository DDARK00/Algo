import sys
from collections import defaultdict
from math import inf
from heapq import heappop, heappush
input = sys.stdin.readline

n, m = map(int,input().split())
# 노드 수 간선 수
g = defaultdict(list)
for _ in range(m):
    a, b , d = map(int,input().split())
    # v1 v2 w
    g[a].append((d,b))
    g[b].append((d,a))
    # w, v

def dijk():
    # 1 -> end
    v_f = [inf]*(n+1) # fox
    v_f[1] = 0
    fox = [(0, 1)] # w, v # pq
    while fox:
        w, v = heappop(fox)
        if v_f[v]<w:
            continue
        for nw, nv in g[v]:

            if v_f[nv]>nw+w:
                v_f[nv] = nw+w
                heappush(fox, (nw+w, nv))

    v_w = [[inf,inf] for _ in range(n+1)] # wolf
    v_w[1][0] = 0
    # 0으로 도착했다고 가정
    wolf = [(0,1,0)] # w,v,2배 0이면 다음 2배 1이 절반
    while wolf:
        w, v, p = heappop(wolf)
        if v_w[v][p] <w:
            continue

        np = 0 if p == 1 else 1
        for nw, nv in g[v]:
            nw = nw/2 if np == 1 else nw*2
            if v_w[nv][np]>w+nw:
                v_w[nv][np] = w+nw
                heappush(wolf,(w+nw,nv,np))

    ans = 0
    for i in range(2,n+1):
        ans += 1 if v_f[i]<min(v_w[i]) else 0
    print(ans)
    return

dijk()