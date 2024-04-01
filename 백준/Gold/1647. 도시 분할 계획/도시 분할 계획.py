import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n, m = map(int, input().split())
# 집의 개수, 길의 개수

edge = [[] for _ in range(n)]

for _ in range(m):
    s, e, w = map(int, input().split())
    edge[s - 1].append((w, e - 1))
    edge[e - 1].append((w, s - 1))

# print(edge)

visited = [0] * n

pq = [(0, 0)]  # w, v

# mst
# visited[0] = 1
cost = 0

k = 0
max_c = 0
while pq:
    w, v = heappop(pq)
    if not visited[v]:
        visited[v] = 1
        cost += w
        max_c = max(max_c, w)
        k += 1
        for x in edge[v]:
            if not visited[x[1]]:
                heappush(pq, x)
    if k == n:
        break

print(cost-max_c)
