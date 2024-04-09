import sys
from math import inf
from heapq import heappop, heappush

input = sys.stdin.readline

n, m, k = map(int, input().split())

visited = [[inf] * (k + 1) for _ in range(n+1)]

g = {}
for i in range(1, n + 1):
    g[i] = []

for _ in range(m):
    a, b, time = map(int, input().split())
    g[a].append((time, b))  # weight, vertex
    g[b].append((time, a))
# 1 -> N 까지의 최소


visited[0] = [0] * (k + 1)

pq = [(0, 1, k)]  # w, v, available change count
# 이렇게 가면 결국 k번 다 써서 완전탐색을 하는 건데 시간이 되나
# print(g)

while pq:
    w, v, cnt = heappop(pq)
    if visited[v][cnt] < w:
        continue

    for nw, nv in g[v]:
        if visited[nv][cnt] > w + nw:
            visited[nv][cnt] = w + nw
            heappush(pq, (w + nw, nv, cnt))
        if cnt > 0:
            if visited[nv][cnt - 1] > w:  # 카운트 쓰기 -> 가중치 안 더하기
                visited[nv][cnt - 1] = w
                heappush(pq, (w, nv, cnt - 1))

print(min(visited[n]))
# print(visited)