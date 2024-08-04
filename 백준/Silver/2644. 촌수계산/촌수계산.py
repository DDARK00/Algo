import sys
from math import inf
from collections import defaultdict
from collections import deque
input = sys.stdin.readline

n = int(input())

a, b = map(int, input().split())
m = int(input())

g = defaultdict(list)

for _ in range(m):
    x, y = map(int,input().split())
    g[x].append(y)
    g[y].append(x)
q = deque([(a,0)])
visited = [inf]*(n+1)
visited[a]=0

while q:
    v, c = q.popleft()
    for nv in g[v]:
        if visited[nv]>c+1:
            q.append((nv,c+1))
            visited[nv]=c+1
print(-1 if visited[b] == inf else visited[b])