import sys
from collections import deque
input = sys.stdin.readline

q = deque([(1,0)])
n = int(input())
m = int(input())

g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [0]*(n+1)
visited[1] = 1

ans = 0
while q:
    v, c = q.popleft()
    for num in g[v]:
        if not visited[num] and c<2:
            q.append((num,c+1))
            visited[num]=1
            ans+=1

print(ans)