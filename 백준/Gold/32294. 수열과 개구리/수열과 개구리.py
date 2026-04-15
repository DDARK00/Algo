import sys
from heapq import heappop, heappush
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
# b시간 a거리
graph=[[]for _ in range(n+1)]
for i, w in enumerate(map(int,input().split())):
    # 100000 *2 *2 w, v
    nv=max(-1,i-a[i])
    nvv=min(n,i+a[i])
    graph[nv].append((w,i))
    graph[nvv].append((w,i))

dist=[float('inf')]*(n+1)
dist[n]=0
pq=[(0,n)] # w v
while pq:
    w, v=heappop(pq)
    if dist[v]<w:
        continue
    for nw, nv in graph[v]:
        if dist[nv]>nw+w:
            dist[nv]=nw+w
            heappush(pq,(nw+w,nv))
print(' '.join(map(str,dist[:-1])))