import heapq
import sys

input = sys.stdin.readline

hq = []

n = int(input())

for _ in range(n):
    a = input().strip()
    if a == "0":
        if hq:
            print(-hq[0])
            heapq.heappop(hq)
        else:
            print(0)
    else:
        a = int(a)
        heapq.heappush(hq, -a)
# heapq . 메소드 (대상배열 ,값)
