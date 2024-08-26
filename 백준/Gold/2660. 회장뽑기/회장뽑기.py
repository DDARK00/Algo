import sys
from collections import deque
from collections import defaultdict
from math import inf
input = sys.stdin.readline

n = int(input())
g = defaultdict(list)

while True:
    a, b = map(int,input().split())
    if a == -1 and b == -1:
        break
    g[a].append(b)
    g[b].append(a)

def bfs(k):
    global low
    visited = [0]*(n+1)
    visited[k] = 1
    q = deque([(k, 0)])

    while q:
        v, c = q.popleft()
        if c>low:
            return inf

        for nv in g[v]:
            if not visited[nv]:
                q.append((nv, c+1))
                visited[nv] = 1
    return c

ans = [0]*(n+1)
low=inf
for i in range(1, n+1):
    temp = bfs(i)
    low = min(temp,low)
    ans[i] = temp

many = 0
out = []
for idx, score in enumerate(ans):
    if score == low:
        many+=1
        out.append(idx)
print(low, many)
print(*out)