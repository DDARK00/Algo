from collections import deque
import sys
input = sys.stdin.readline

n, m, v =map(int, input().split())

# n정점 m간선 v시작

graph={}
for _ in range(m):
    s, e =map(int, input().split())
    if graph.get(s):
        graph[s].append(e)
    else:
        graph[s] = [e]
    if graph.get(e):
        graph[e].append(s)
    else:
        graph[e] = [s]
# print(graph)

#bfs
b_visited= []
que = deque([v])

while que:
    node = que.popleft()
    # print(node)
    if node not in b_visited:
        b_visited.append(node)
        if graph.get(node) :
            que.extend(sorted(graph[node],key=lambda x : x))
        


#dfs

d_visited =[]
stack = [v]
while stack:
    node = stack.pop()
    if node not in d_visited:
        d_visited.append(node)
        if graph.get(node):
            stack.extend(sorted(graph[node],key= lambda x: -x))

print(*d_visited)
print(*b_visited)