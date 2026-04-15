import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
graph=[[]for _ in range(n+1)]

for i in range(1,1+n):
    k=int(input())
    graph[i].append(k)

ans=[]
q=deque([])
for i in range(1,1+n):
    visited=[0]*(n+1)
    visited[i]=1
    q.append(i)
    cnt=1
    visited[i]=1
    while q:
        v=q.popleft()
        for nv in graph[v]:
            if not visited[nv]:
                cnt+=1
                visited[nv]=1
                q.append(nv)
    ans.append((i,cnt))
ans.sort(key=lambda x:(-x[1],x[0]))
print(ans[0][0])