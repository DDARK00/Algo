import sys
from heapq import heappop, heappush

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())

    pq = []

    weight = 0
    for a in list(map(int, input().split())):
        # 머지인가 했는데 그냥 작은거끼리 합치는거?
        heappush(pq, a)

    while len(pq) > 1:
        a = heappop(pq)
        b = heappop(pq)
        weight += a
        weight += b
        heappush(pq, a + b)
    print(weight)