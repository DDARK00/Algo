import sys
from collections import defaultdict
from math import inf
input = sys.stdin.readline

n, m = map(int,input().split())
g = defaultdict(list)

for _ in range(m):
    a, b, c = map(int,input().split())
    g[a].append((b,c)) # v, w
    # g[b].append((a,c))

def bell(start):
    dist = [inf]*(n+1) #1~n
    dist[start] = 0
    for _ in range(n-1):
        for now in range(1,1+n):
            for to, cost in g[now]:
                if dist[now]+cost < dist[to]:
                    dist[to] = dist[now]+cost
    for now in range(1,1+n):
        for to, cost in g[now]:
            if dist[now] != inf and dist[now]+cost < dist[to]:
                print(-1)
                exit()
    return dist

ans = bell(1)
for i in range(2,n+1):
    print(ans[i] if ans[i] != inf else -1)