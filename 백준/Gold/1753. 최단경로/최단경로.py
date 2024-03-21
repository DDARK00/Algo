import sys
from heapq import heappop, heappush
from math import inf

input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())

graph = {}

for i in range(V):
    graph[i] = []
for _ in range(E):
    a, b, c = map(int, input().split())

    graph[a - 1].append((b - 1, c))
    # graph[b].append((a, c))

# 그래프 작성 -> 힙큐에 때려박기
# 하면서 거리 비용 갱신

distance = [inf] * (V)

hq = []

heappush(hq, (0, start - 1))  # 비용과 노드
distance[start - 1] = 0

while hq:
    w, v = heappop(hq)

    if distance[v] < w:
        continue

    for next_node, next_dist in graph[v]:
        cost = w + next_dist
        # print("dist :", next_dist, "// node : ", next_node)
        if distance[next_node] > cost:
            distance[next_node] = cost
            heappush(hq, (cost, next_node))

for val in distance:

    if type(val) != float:
        print(val)
    else:
        print("INF")