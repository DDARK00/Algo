import sys
from collections import defaultdict
from heapq import heappop, heappush
input=sys.stdin.readline

def sol(n, m):
    # n, m = map(int, input().split())
    g = defaultdict(list)
    # 1->n

    for _ in range(m):
        a, b, p = map(int, input().split())
        p/=100
        g[a].append((p, b))
        g[b].append((p, a))
    # int(input().rstrip())

    pq = [(-1, 1)] # percent, v
    per = [0]*(n+1)
    per[1] = 1
    # 100 -1  50 -0.5   0  0

    while pq:
        p, v = heappop(pq)
        p *= -1
        if per[v] > p:
            continue

        for np, nv in g[v]:
            if per[nv] >= p*np:
                continue
            per[nv] = p*np
            heappush(pq, (-(p*np), nv))

    print(f'{per[n]*100:6f} percent')
while True:
    tc = input().rstrip()
    if tc == "0":
        break
    sol(*map(int, tc.split()))