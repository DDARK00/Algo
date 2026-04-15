import sys
from collections import deque, defaultdict
input=sys.stdin.readline
n,m=map(int,input().split())

g=defaultdict(list)
for _ in range(m):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    g[a].append(b)
    g[b].append(a)

for _ in range(int(input())):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    g[a].append(b)
    g[b].append(a)
    visited=[-1]*(n)
    q=deque([(0,0)])
    visited[0]=0
    while q:
        v,c=q.popleft()
        for nv in g[v]:
            if visited[nv]==-1:
                visited[nv]=c+1
                q.append((nv,c+1))
    print(*visited)