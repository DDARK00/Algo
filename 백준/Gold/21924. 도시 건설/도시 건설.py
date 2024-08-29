import sys
from collections import defaultdict
from heapq import heappop, heappush

input = sys.stdin.readline

n, m = map(int,input().split())
g = defaultdict(list)
total = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((c,b))
    g[b].append((c,a))
    total+=c

# 1부터 시작
pq = [(0, 1)] # w, v
visited = [0]*(n+1)
cost = 0
cnt = 0
while pq:
    w, v = heappop(pq)
    if not visited[v]:
        visited[v] = 1
        cost+=w
        cnt+=1
        for nw, nv in g[v]:
            if not visited[nv]:
                heappush(pq, (nw,nv))
        if cnt ==n:
            break

if n == cnt:
    print(total-cost)

else:
    print(-1)