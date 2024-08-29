import sys

from heapq import heappush, heappop

from math import inf

input = sys.stdin.readline

Tc = int(input())

for _ in range(Tc):

    n, d, c = map(int,input().split())

    # 컴 의존성 스타트

    g = {}

    for i in range(1,n+1):

        g[i] = []

        

    for _ in range(d):

        a,b,s = map(int,input().split())

        # g[a].append((s,b))

        g[b].append((s,a))

    # dijk

    pq = [(0,c)]

    cost = [inf]*(n+1)

    cost[c]=0

    vset = {c}

    m_cost = 0

    while pq:

        w, v = heappop(pq)

        if cost[v]<w:

            continue

        m_cost = max(m_cost, w)

        for nw, nv in g[v]:

            if cost[nv]>w+nw:

                cost[nv] = w+nw

                vset.add(nv)

                heappush(pq, (w+nw,nv))

    # print(cost)

    print(len(vset), m_cost)

    