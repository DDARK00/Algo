import sys

input = sys.stdin.readline

# 첫째 줄에 사람의 수 N (5 ≤ N ≤ 2000)과 친구 관계의 수 M (1 ≤ M ≤ 2000)이 주어진다.

n, m = map(int, input().split())

obj = {}
for i in range(n):
    obj[i] = []

for _ in range(m):
    a, b = map(int, input().split())
    obj[a].append(b)
    obj[b].append(a)

# print(obj)

visited = [0] * n


def dfs(depth, k):
    global find
    if find:
        return
    if depth == 5:
        find = True
        return

    if not visited[k] and obj.get(k):

        visited[k] = 1
        for v in obj[k]:
            dfs(depth + 1, v)
        visited[k] = 0

find = False
for i in range(n):
    if find:
        break
    dfs(0, i)
print(1 if find else 0)
