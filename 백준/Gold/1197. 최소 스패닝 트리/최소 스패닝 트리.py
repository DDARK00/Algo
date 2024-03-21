import sys

input = sys.stdin.readline

v, e = map(int, input().split())

edges = []

for _ in range(e):
    a, b, w = map(int, input().split())
    edges.append([a-1, b-1, w])
edges.sort(key=lambda x: x[2])

p_lst = [i for i in range(v)]


def p_find(x):
    p = p_lst[x]
    if x != p:
        p = p_find(p_lst[x])
    p_lst[x] = p
    return p


def union(x, y):
    x = p_find(x)
    y = p_find(y)
    if x == y:
        return

    if x < y:
        p_lst[y] = x
    else:
        p_lst[x] = y


weight = 0
cnt = 0
for s, e, w in edges:
    if p_find(s) == p_find(e):
        continue

    weight += w
    union(s, e)
    cnt += 1
    if cnt == v - 1:
        break
print(weight)
