import sys
from collections import defaultdict
from heapq import heappop, heappush
input=sys.stdin.readline

n, d=map(int,input().split()) # 지름길 수, 도로 길이

g=defaultdict(list)

# n=12
v=set()
v.add(0)
for _ in range(n):
    st,ed,l=map(int,input().split())
    if ed>d:
        continue
    g[st].append((l,ed))
    g[ed].append((d-ed,d))
    v.add(st)
    v.add(ed)

g[0].append((d,d))
v=list(sorted(list(v)))
for i in range(len(v)-1):
    for j in range(i+1,len(v)):
        g[v[i]].append((v[j]-v[i],v[j])) # c, v
        g[v[i]].append((d-v[i],d))

pq=[(0,0)] # c, v
cost=defaultdict(lambda : float('inf'))
cost[0]=0;
while pq:
    c, v =heappop(pq)
    if cost[v]<c:
        continue

    for nc, nv in g[v]:
        if cost[nv]>nc+c:
            cost[nv]=nc+c
            heappush(pq,(nc+c,nv))
print(cost[d])