import sys
from heapq import heappop, heappush, heapify
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    # 테케 수
    n = int(input())

    # 슬라임수 <=60
    ans = 1
    pq = list(map(int,input().split()))
    heapify(pq) # 60개면 가능
    # 최솟값을 1, 000, 000, 007로 나눈 나머지 
    while len(pq)!=1:
        a = heappop(pq)
        b = heappop(pq)
        ans = ans * a*b % 1000000007
        heappush(pq,a*b)
    print(ans)