import sys
from collections import deque
from collections import defaultdict
from math import inf
input = sys.stdin.readline

g = defaultdict(list)
q = deque()
n, m, want, start = map(int, input().split())

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)

cost = [inf]*(n+1)
cost[start] = 0
q.append((start,0))

while q:
    v, w = q.popleft()

    if cost[v]<w:
        continue

    for nv in g[v]:
        if cost[nv]>w+1:
            cost[nv] = w+1
            q.append((nv,w+1))

find=False
for idx, val in enumerate(cost):
    if val==want:
        print(idx)
        find = True

if not find:
    print(-1)