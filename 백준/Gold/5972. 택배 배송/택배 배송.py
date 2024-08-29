import sys

from math import inf

from heapq import heappop, heappush

input = sys.stdin.readline

n, m = map(int,input().split())

g = {}

for i in range(n):

    g[i] = []

for _ in range(m):

    a, b, w = map(int,input().split())

    

    g[a-1].append((w,b-1))

    g[b-1].append((w,a-1))

    

# v, w

# print(g)

def dijk():

    visited = [inf]*n

    visited[0] = 0

    pq = [(0,0)]

    while pq:

        w,v = heappop(pq)

        # print(v)

        if v == n-1:

            print(w)

            break

        for nw, nv in g[v]:

            # print(nw,nv)

            

            if visited[nv]>nw+w:

                visited[nv] = nw+w

                heappush(pq,(nw+w,nv))

    

# 1 -> n 

# 1<= n <=50000

dijk()

