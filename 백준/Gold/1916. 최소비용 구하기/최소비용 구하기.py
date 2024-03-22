import sys
from math import inf
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())  # 도시의 수
m = int(input())  # 버스의 수

bus_sch = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    bus_sch[a - 1].append((c, b - 1))
    # bus_sch[b - 1].append((c, a - 1))
start, end = map(int, input().split())
start -= 1
end -= 1

all_cost = [inf] * n

pq = [(0, start)]
all_cost[start] = 0

while pq:
    cost, city_num = heappop(pq)

    if city_num == end:
        print(cost)
        break

    if all_cost[city_num] < cost:
        continue

    for n_cost, goto in bus_sch[city_num]:
        # print(cost, city_num,n_cost,cost)
        if all_cost[goto] > n_cost + cost:
            all_cost[goto] = n_cost + cost
            heappush(pq, (n_cost + cost, goto))
# print(all_cost)
# 버스라서 왕복 가능한줄..?
