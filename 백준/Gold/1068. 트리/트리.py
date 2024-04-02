import sys

input = sys.stdin.readline

n = int(input())  # 노드의수

lst = list(map(int, input().split()))

# 부모노드번호

g = [[] for _ in range(n)]

k = int(input())
start = None
for i in range(n):
    if i == k:
        continue
    if lst[i] != -1 and lst[i] != k:  # lst[i] 부모노드

        g[lst[i]].append(i)

    elif lst[i] == -1:

        start = i

# 지울노드번호

# dfs
if start != None:
    st = [start]
else:
    st = []

visited = [0] * n

cnt = 0
# print(g, start)
while st:
    v = st.pop()

    if not visited[v]:

        visited[v] = 1

        if g[v]:
            # if g[v][0] == k:
            #
            st.extend(g[v])

        else:

            cnt += 1

print(cnt)

