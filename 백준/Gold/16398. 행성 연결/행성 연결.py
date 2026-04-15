import sys
from collections import defaultdict
from heapq import heappop, heappush
input=sys.stdin.readline

n=int(input())
pq=[]

g=defaultdict(list)
for i in range(1,1+n):
    for j, cost in enumerate(map(int,input().split())):
        g[i].append((cost,j+1))
# cost, nv
visited=[0]*(n+1)
ok=0
pq.append((0,0)) # cost v
g[0].append((0,1))
answer=0
while pq:
    c,v=heappop(pq)
    if visited[v]:
        continue
    ok+=1
    answer+=c
    visited[v]=1
    if ok==n+1:
        break
    for nc,nv in g[v]:
        if not visited[nv]:
            heappush(pq,(nc,nv))
print(answer)