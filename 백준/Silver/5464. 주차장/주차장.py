import sys

from collections import deque

from heapq import heappop, heappush

input = sys.stdin.readline

n, m = map(int, input().split())

# 비용

cost = [0]+[int(input()) for _ in range(n)]

# 무게

weight = [0]+[int(input()) for _ in range(m)]

# 차댄곳

seat = [0] * (m+1)

# 대기열

q = deque([])

# 주차장

park = [i for i in range(1, n+1)]

answer = 0

for _ in range(2*m):

    k = int(input())

    if k>0: # 들어오면

        if park:

            seat[k] = heappop(park)

        else:

            q.append(k)

    else:

        k = -k

        fee = cost[seat[k]]*weight[k]

        answer+= fee

        if q:

            seat[q[0]] = seat[k]

            q.popleft()

        else:

            heappush(park, seat[k])

print(answer)