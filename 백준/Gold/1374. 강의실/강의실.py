import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())

lst = [tuple(map(int,input().split())) for _ in range(n)]
lst.sort(key=lambda x:x[1])
pq = []
for idx, s, e in lst:
    if pq and pq[0] <=s:
        heappop(pq)
    heappush(pq,e)
print(len(pq))