import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

g = {}

for i in range(1, n + 1):
    g[i] = []
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

start = 1

q = deque([(start, start)])
lst = [0] * (n + 1)

while q:
    v, paren = q.popleft()

    if not lst[v]:
        lst[v] = paren
        child = g[v]
        for c in child:
            if not lst[c]:
                q.append((c, v))

for i in range(2, n + 1):
    print(lst[i])
