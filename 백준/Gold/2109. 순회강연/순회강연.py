import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[1])  # 일자로 정렬
pq = []
for i in range(n):
    heappush(pq, arr[i][0])

    if len(pq) > arr[i][1]:  # len(가능한 일자) 유지하면서 가장 작은 금액 빼기
        heappop(pq)

result = sum(pq)
print(result)
