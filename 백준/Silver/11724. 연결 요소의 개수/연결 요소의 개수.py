import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

g = [[] for _ in range(n + 1)]
# g = {}

# for i in range(1, n + 1):
#     g[i] = []

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

# print(g)

q = deque([])
# bfs

# visited = {}
visited = [0] * (n + 1)
cnt = 0

for val in range(1, n + 1):
    if not visited[val]:
        q.append(val)

        cnt += 1

        while q:
            v = q.popleft()
            if not visited[v]:
                visited[v] = 1
                if g[v]:
                    q.extend(g[v])

print(cnt)
# print(g)
# 딕셔너리 -> 리스트로 바꿔봤음