import sys
from heapq import heappop, heappush
from math import inf

input = sys.stdin.readline

n = int(input())  # 도시
m = int(input())  # 버스

city_list = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    city_list[a - 1].append((c, b - 1))
    # city_list[b - 1].append((c, a - 1))

for i in range(n):
    distance = [inf] * n
    pq = [(0, i)]
    distance[i] = 0
    # 출력~~
    while pq:
        cost, v = heappop(pq)

        if distance[v] < cost:
            continue

        for nc, nv in city_list[v]:
            if distance[nv] > nc + cost:
                distance[nv] = nc + cost
                heappush(pq, (nc + cost, nv))

    ans = map(str, distance)
    ans = " ".join(ans).replace('inf', '0')
    print(ans)