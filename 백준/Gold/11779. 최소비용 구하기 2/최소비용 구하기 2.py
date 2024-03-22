import sys
from math import inf
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())  # 도시
m = int(input())  # 버스

g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((c, b))
    # g[b - 1].append((c, a - 1))
# 그래프 작성

start, end = map(int, input().split())
# 시작, 끝

pq = [(0, start)]  # 비용, 노드

dist = [inf] * (n+1)  # 총 비용
dist[start] = 0

howto = [i for i in range(n+1)]  # 현재 지역으로 오려면 어디를 통해서 와야 최소 비용인가 (부모노드)

while pq:
    c, v = heappop(pq)

    if dist[v] < c:
        continue

    for nc, nv in g[v]:  # 다음에 갈 경로
        if dist[nv] > nc + c:
            dist[nv] = nc + c
            howto[nv] = v

            heappush(pq, (nc + c, nv))


print(dist[end] if str(dist[end]) != 'inf' else '0')
idx = end
ans = ""
cnt = 0
while idx != start:
    cnt += 1
    ans = str(idx) + " " + ans
    idx = howto[idx]
else:
    cnt += 1
    ans = str(start) + " " + ans
print(cnt)
print(ans)
