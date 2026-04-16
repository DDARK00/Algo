import sys
from collections import deque,defaultdict
input=sys.stdin.readline

n,m,r=map(int,input().split())
q=deque([r-1])
visited=[-1]*n
visited[r-1]=0
g=defaultdict(list)
for _ in range(m):
    u,v=map(int,input().split())
    u,v=u-1,v-1
    g[u].append(v)
    g[v].append(u)

while q:
    v=q.popleft()
    for nv in g[v]:
        if visited[nv]==-1:
            visited[nv]=visited[v]+1
            q.append(nv)

print(*visited,sep='\n')