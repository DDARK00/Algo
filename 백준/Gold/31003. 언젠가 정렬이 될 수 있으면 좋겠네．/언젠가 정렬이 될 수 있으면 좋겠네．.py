import sys
from heapq import heappop, heappush
from math import gcd
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))

pq = []

g = [[] for _ in range(n)]
level = [0] * n
for idx, num in enumerate(lst):
    for i in range(idx+1, n):
        if(num != lst[i] and gcd(num, lst[i]) != 1):
            g[idx].append(i)
            # g[i].append(idx)
            level[i] += 1

for i in range(n):
    if level[i] == 0:
        heappush(pq, (lst[i], i))

while pq:
    val, idx = heappop(pq)
    print(val, end=' ')
    for i in g[idx]:
        level[i] -=1
        if level[i] == 0:
            level[i] = -1
            heappush(pq, (lst[i],i))
