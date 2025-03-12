import sys
from collections import defaultdict
input=sys.stdin.readline

n, m = map(int, input().split())

g = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    # b -> a
    g[b].append(a)

ans = [[0,i] for i in range(n+1)]

st = []
for i in range(1, n+1):
    st.append(i)
    visited = [0]*(n+1)
    visited[i]=1
    t = 1
    while st:
        v = st.pop()
        for nv in g[v]:
            if not visited[nv]:
                t+=1
                visited[nv]=1
                st.append(nv)
    ans[i][0] = t
ans.sort(key=lambda x:(-x[0], x[1]))

k = ans[0][0]
for c, v in ans:
    if c!=k:
        break
    print(v, end=" ")