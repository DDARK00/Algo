import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())  # n개의 노드와 m개의 노드쌍(q)

tree = {}
for i in range(n):
    tree[i] = []
for _ in range(n - 1):
    a, b, w = map(int, input().split())
    # start, end, length
    tree[a - 1].append((b - 1, w))
    tree[b - 1].append((a - 1, w))

# print(tree)

for _ in range(m):
    visited = [2147483640] * n

    a, b = map(int, input().split())
    q = deque([(a - 1, 0)])

    while q:
        v, cost = q.popleft()
        if v == b-1:
            print(cost)
            break
        if visited[v] > cost:
            visited[v] = cost

            for nv, nc in tree.get(v):
                q.append((nv, nc + cost))
