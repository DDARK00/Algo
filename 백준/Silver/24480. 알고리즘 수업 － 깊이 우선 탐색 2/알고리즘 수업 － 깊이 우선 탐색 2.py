import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

g = {}

n, m, r = map(int, input().split())

# 정점의 수, 간선의 수, 시작 정점

for i in range(n+1):

    g[i] = []

for i in range(m):

    a, b = map(int, input().split())

    g[a].append(b)

    g[b].append(a)

# print(g)

visited = [0] * (n + 1)

def dfs(e: dict, r: int):  # 정점 집합, 간선 집합, 시작 정점

    global cnt

    visited[r] = cnt

    

    g[r].sort(key=lambda x: -x)

    

    for el in g[r]:

        if not visited[el]:

            

            cnt+=1

            dfs(e, el,)

cnt = 1

dfs(g, r)

for i in range(1, n + 1):

    print(visited[i])

