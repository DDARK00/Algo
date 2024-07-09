import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n = int(input())
lecture = [tuple(map(int,input().split())) for _ in range(n)]
lecture.sort() # start

pq = []
for s, e in lecture:
    if pq and pq[0]<=s:
        heappop(pq)
    heappush(pq,e)
print(len(pq))