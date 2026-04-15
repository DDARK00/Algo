import sys
from heapq import heappop, heappush
input=sys.stdin.readline

n, q = map(int,input().split())

pq = []
for i in range(q):
    a, b, x = map(int,input().split())
    heappush(pq, (a,i,b,x))
    # s, priority, e, color

now = [] # pq
for i in range(1, n+1):
    while pq and pq[0][0] ==i:
        nst, *rest = heappop(pq)
        heappush(now, (rest))
    while now and now[0][1]<i:
        heappop(now)
    if now:
        print(now[0][2], end=" ")
    else:
        print(0, end=" ")