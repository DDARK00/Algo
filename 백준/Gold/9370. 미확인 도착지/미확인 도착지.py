import sys

from heapq import heappop, heappush

from math import inf

input = sys.stdin.readline

Tc = int(input())

def dijk(start):

    dist[start] = [0,start] # w, from v

    pq = [(0,start,0)]

    

    while pq:

        w, v, f = heappop(pq)

        if dist[v][0]<w:

            continue

        for nw, nv in graph[v]:

            if dist[nv][0]> nw+w:

                dist[nv][0] = nw+w

                

                if chk.get(v) and chk.get(nv):

                    heappush(pq,(nw+w,nv,1))

                    dist[nv][1] = 1

                else:

                    

                    heappush(pq,(nw+w,nv,f))

                    dist[nv][1] = f

    

for _ in range(Tc):

    n, m, t = map(int,input().split())

    # 노드 수 간선 수 목적지 수

    s, g, h = map(int,input().split())

    # 시작점, 목적지까지 포함되어야 하는 노드

    graph = {}

    for i in range(1,n+1):

        graph[i] = []

    chk = {g:1, h:1}

    for _ in range(m):

        a,b,d = map(int,input().split())

        if chk.get(a) and chk.get(b):

            graph[a].append((d-0.01,b))

            graph[b].append((d-0.01,a))

        else:

            graph[a].append((d,b))

            graph[b].append((d,a))

        # w, v

    # print(graph)

    dist = [[inf,0] for _ in range(1+n)]

    dijk(s)

    # print(g,h)

    answer = []

    for _ in range(t):

        x = int(input())

        # print(dist)

            

        if dist[x][1]:

            answer.append(x)

    print(*sorted(answer))