import sys
from collections import deque, defaultdict
input=sys.stdin.readline
n,m=map(int,input().split())
s,e=map(int,input().split())
g=defaultdict(list)
for _ in range(m):
    x,y=map(int,input().split())
    g[x].append(y)
    g[y].append(x)

visited=[0]*(n+1)
visited[s]=1
q=deque([s])
while q:
    v=q.popleft()
    for nv in g[v]+[v+1,v-1]:
        if 0<nv<=n and not visited[nv]:
            q.append(nv)
            visited[nv]=visited[v]+1
print(visited[e]-1)