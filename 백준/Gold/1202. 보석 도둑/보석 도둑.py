import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n, k = map(int, input().split())
# 보석 수, 가방 수

g=[tuple(map(int,input().split())) for _ in range(n)]
g.sort(key = lambda x : x[0])
# 무게 가격->무게순

b = [int(input()) for _ in range(k)]
#가방
b.sort()

pq = []

money = 0
g_idx = 0

for m in b:

    while g_idx<n and g[g_idx][0]<=m:
        heappush(pq,- g[g_idx][1])
        g_idx+=1
        # 가능한 보석
    # print(pq, m, g_idx, n , g_idx<n)

    try:
        money+= -(heappop(pq))
            # 가능한 보석 중 제일 비싼거

    except:
        continue
        # 담을게 없을때

#이러면 복잡도가 얼마나 나오지
# 아오 3퍼컷
print(money)