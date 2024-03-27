import sys

from math import inf

from heapq import heappush, heappop

input = sys.stdin.readline

n, m, x = map(int,input().split())

# n명이 x번 마을에 모인다

g = {}

r_g = {}

# 그래프, 리버스 그래프

# x e -> s 거리 오는길ㅇ

# r_s ->거리 가는길ㄱ

for i in range(1,n+1):

    g[i] = []

    r_g[i] = []

    

for _ in range(m):

    # A에서 다른 도시 B로 가는 도로의 개수는 최대 1개이다.

    s, e, t = map(int,input().split())

    g[s].append((t,e))

    r_g[e].append((t,s))

def dijk(start):

    pq = [(0, start)] # 비용 노드

    dist = [inf]*(n+1)

    dist[start] = 0

    dist[0] = 0

    while pq:

        w, v = heappop(pq)

        if dist[v]<w:

            continue

        # print(g[v])

        for nw, nv in g[v]:

            if dist[nv] > w+nw:

                dist[nv] = w+nw

                heappush(pq,(w+nw,nv))

        

    return dist

d1 = dijk(x)

g = r_g

d2 = dijk(x)

print(max(map(sum,(map(list,zip(d1,d2))))))