import sys
from heapq import heapify, heappop, heappush
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]
heapify(lst)
while len(lst)>1:
    a, b = heappop(lst), heappop(lst)
    heappush(lst,(a+b)/2)
print(lst[0])