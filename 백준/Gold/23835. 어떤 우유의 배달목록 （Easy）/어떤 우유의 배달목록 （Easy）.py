import sys
input = sys.stdin.readline

n = int(input())
# 노드의 개수

graph = {}
for _ in range(n-1):
    a,b = map(int,input().split())
    # 이동할 수 있는 경로가 정확히 한 개 있다.
    if graph.get(a):
        graph[a].append(b)
    else:
        graph[a] = [b]

    if graph.get(b):
        graph[b].append(a)
    else:
        graph[b] = [a]
# 그래프 작성



q = int(input())
# 쿼리의 수
milk = [0]*(n+1)

# dfs
def dfs(st, ed):
    if st==ed:
        for pack, room in enumerate(route):
            milk[room]+=pack
        # print(route)
        return
    if not visited[st]:
        visited[st]=1
        if graph.get(st):
            node = graph[st]
            for v in node:
                route.append(v)
                dfs(v,ed)
                route.pop()
                # 시작점이 자꾸 없더니 자식 노드 처리만 하고 있었음

for _ in range(q):
    order = list(map(int,input().split()))

    if order[0] == 1:
        visited = [0]*(n+1)
        route = [order[1]]
        dfs(order[1], order[2])
    else:
        print(milk[order[1]])