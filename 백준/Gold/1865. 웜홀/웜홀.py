import sys
# from math import inf
from collections import defaultdict
input = sys.stdin.readline

tc = int(input())

def bellman_ford(start):
    dist = [10000000]*(n+1) # 1~n
    # n-1, 500, 10000
    # dist[start] = 0

    for _ in range(n-1):
        for i in range(1,n+1):
            for v, w in g[i]:
                if dist[i]+w < dist[v]:
                    dist[v] = dist[i]+w

    for i in range(1,n+1): # cycle check
        for v, w in g[i]:
            if dist[i]+w < dist[v]:
                print("YES")
                return
    print("NO")
    return


for _ in range(tc):
    n, m, w = map(int,input().split())
    g = defaultdict(list)
    for _ in range(m):
        s, e, t = map(int,input().split())
        g[s].append((e,t)) # v, w
        g[e].append((s,t))
    
    for _ in range(w):
        s, e, t = map(int,input().split())
        g[s].append((e,-t))

    bellman_ford(1)