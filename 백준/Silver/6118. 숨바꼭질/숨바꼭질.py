import sys
from collections import deque
input=sys.stdin.readline

n, m = map(int, input().split())

g = {}
for i in range(1, n+1):
    g[i] = []

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [0]*(n+1)
visited[1] = 1
ans = {}

q = deque([(1, 0)]) # v, c
while q:
    v, c = q.popleft()
    for nv in g[v]:
        if not visited[nv]:
            visited[nv]=c+1
            if ans.get(c+1):
                ans[c+1].append(nv)
            else:
                ans[c+1]=[nv]
            q.append((nv, c+1))
print(min(ans[c]),c,len(ans[c]))