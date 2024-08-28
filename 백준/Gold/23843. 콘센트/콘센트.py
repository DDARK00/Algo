import sys
from heapq import heappop,heappush
input = sys.stdin.readline

n, m = map(int, input().split())
pq = [0]*(m)

lst = list(map(int,input().split()))

lst.sort(reverse=True)

for num in lst:
    added = heappop(pq) + num
    heappush(pq, added)
print(max(pq))