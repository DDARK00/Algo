import sys
from collections import defaultdict
input=sys.stdin.readline

n=int(input())
colors=[0]+list(map(int,input().split()))
g=defaultdict(list)
for _ in range(n-1):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)

answer=0
visited=[0]*(n+1)
visited[1]=1
st=[(1,0)]
while st:
    v,c=st.pop() # v, p로부터 받은 color
    if colors[v]!=0 and colors[v]!=c:
        answer+=1
        c=colors[v]
    for nv in g[v]:
        if visited[nv]:continue
        visited[nv]=1
        st.append((nv,c))
print(answer)