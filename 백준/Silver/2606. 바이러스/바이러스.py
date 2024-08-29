import sys
from collections import deque
input = sys.stdin.readline

n= int(input())
v= int(input())
# 점 선 수

g = {}
for _ in range(v):
    a, b = map(int, input().split())
    if g.get(a) :
        g[a].append(b)
    else:
        g[a] = [b]

    if g.get(b):
        g[b].append(a)
    else:
        g[b] = [a]
# 그래프

visit = []
q = deque([1])

while q:
    node = q.popleft()
    if node not in visit:
        visit.append(node)
        if g.get(node):
            q.extend(g[node])
print(len(visit)-1)
# 1번제외