import sys
from collections import deque
input=sys.stdin.readline

a,b,n,m=map(int,input().split()+input().split())

q=deque([a])
g=[[]for _ in range(n+1)]
for x,y in [map(int,input().split()) for _ in range(m)]:
    g[x].append(y)
    g[y].append(x)

visited=[-1]*(n+1)
visited[a]=0

while q:
    v=q.popleft()
    for nv in g[v]:
        if visited[nv]==-1:
            visited[nv]=visited[v]+1
            q.append(nv)
print(visited[b])