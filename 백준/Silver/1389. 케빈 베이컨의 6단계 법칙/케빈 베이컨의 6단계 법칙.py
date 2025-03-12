import sys
from collections import deque, defaultdict
input=sys.stdin.readline

n, m = map(int, input().split())

ans = [[float('inf')]*(n) for _ in range(n)]

g = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    g[a].append(b)
    g[b].append(a)

for i in range(n):
    q = deque([(i,0)])
    ans[i][i] = 0
    while q:
        v, c = q.popleft()
        for nv in g[v]:
            if ans[i][nv] == float('inf'):
                ans[i][nv] = c+1
                q.append((nv, c+1))

rst = [1, sum(ans[0])]
for i in range(1, n):
    temp=sum(ans[i])
    if temp<rst[1]:
        rst = [i+1, temp]
print(rst[0])