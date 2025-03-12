import sys
from collections import defaultdict
from heapq import heappop, heappush
input=sys.stdin.readline

n = int(input())

g = defaultdict(list)
day_max = 0
for _ in range(n):
    d, w = map(int, input().split())
    g[d].append(w)
    day_max = max(day_max, d)
pq = []

ans = 0
for i in range(day_max,0,-1):
    for w in g[i]:
        heappush(pq, -w)
    if pq:
        ans += -heappop(pq)
print(ans)