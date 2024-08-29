import sys
from collections import defaultdict
input=sys.stdin.readline

n, m = map(int,input().split())
g = defaultdict(list)

for _ in range(m):
    a, b = map(int,input().split())
    g[b].append(a)
x = int(input())

st = [x]
ans = 0
visited = [0]*(n+1)
visited[x]=0
while st:
    v = st.pop()
    for nv in g[v]:
        if not visited[nv]:
            visited[nv]=1
            ans+=1
            st.append(nv)
print(ans)