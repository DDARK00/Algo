import sys

from math import inf

from heapq import heappop, heappush

input = sys.stdin.readline

n, e = map(int, input().split())

# 정점 간선 수

g = {}

for i in range(1, n+1):

    g[i] = []

for _ in range(e):

    a, b, c = map(int,input().split())

    g[a].append((b,c))

    g[b].append((a,c))

def dijk(start, end):

    

    hq = [(0,start)] # 비용, 노드

    dist = [inf for _ in range(n+1)]

    

    dist[start] = 0

 

    weight = 0

    while hq:

        w, v = heappop(hq)

        # print(w,v,end)

        

        if dist[v]<w:

            continue

        weight += w

        

        if v == end:

            return dist[v]

        for nv, nw in g[v]:

            if dist[nv]>w+nw:

                dist[nv] = w+nw

                heappush(hq, (w+nw,nv))

        

        

    return -1

v1, v2 = map(int,input().split())

ans1_1 = dijk(1,v1)

ans1_2 = dijk(v1,v2)

ans1_3 = dijk(v2,n)

if ans1_1 >=0 and ans1_2>=0 and ans1_3>=0:

    

    ans2_1 = dijk(1,v2)

    ans2_2 = dijk(v2,v1)

    ans2_3 = dijk(v1,n)

    print(min(ans1_1+ans1_2+ans1_3,ans2_1+ans2_2+ans2_3))

else:

    print(-1)

                

# 3 2 1 4