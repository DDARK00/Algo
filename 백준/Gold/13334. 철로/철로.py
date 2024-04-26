from heapq import heappop, heappush
import sys

input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
    a, b = map(int, input().split())

    lst.append((min(a, b), max(a, b)))
L = int(input())
lst.sort(key=lambda x: x[1])
# print(lst)
pq = []
now = 0
mx_now = 0
for start, end in lst:
    while pq and pq[0][0] < end - L:
        # print(pq[0])
        heappop(pq)
        now-=1
    if end - L <= start:
        heappush(pq, (start, end))
        now += 1
        mx_now = max(mx_now, now)
print(mx_now)