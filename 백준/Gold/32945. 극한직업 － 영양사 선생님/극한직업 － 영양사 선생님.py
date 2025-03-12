import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
lst.sort(reverse=True)
pq = []
ans = 0

for idx, n in enumerate(lst):
    heappush(pq, idx+n) # 끝나는 턴
    while pq and pq[0]<=idx:
        heappop(pq)
    ans = max(ans, len(pq))
print(ans)