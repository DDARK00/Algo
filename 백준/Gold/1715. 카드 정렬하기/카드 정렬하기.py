import sys

from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())

pq = []

for _ in range(n):

    heappush(pq,int(input()))

ans = 0

while len(pq)>1:

    a,b = heappop(pq), heappop(pq)

    daum = a+b

    ans+= daum

    heappush(pq,daum)

print(ans)