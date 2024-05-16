import sys
from heapq import heappop, heapify, heappush

input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    lst = list(map(int, input().split()))
    answer = 0
    heapify(lst)
    # print(lst)
    while len(lst) > 1:
        a, b = heappop(lst), heappop(lst)
        answer = answer + a + b
        heappush(lst, a + b)
    print(answer)
