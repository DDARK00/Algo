import sys
import heapq

input = sys.stdin.readline
lst = []

n = int(input())

for _ in range(n):
    k = input().rstrip()
    # print(lst, k)
    # print(k == '0')
    if k == '0':
        if not lst:
            print(0)
        else:
            print(heapq.heappop(lst))
    else:
        heapq.heappush(lst, int(k))
