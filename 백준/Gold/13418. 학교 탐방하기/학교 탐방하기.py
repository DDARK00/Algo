import sys
from heapq import heappop, heappush
input=sys.stdin.readline
 
# init
n, m = map(int, input().split())
g = [[]for _ in range(n+2)]
 
for _ in range(m+1):
    a,b,w = map(int, input().split())
    g[a].append((w^1,b))
    g[b].append((w^1,a))
 
g[n+1].append((0,0))
 
def prim(flag):
    chk = [0]*(n+2)
    pq = [(0,n+1)] # w, v
 
    cnt = 0
    ans = 0
    while pq:
        w, v = heappop(pq)
        if chk[v]:
            continue
        chk[v]=1
        cnt+=1
        ans+=w*flag
        if cnt == n+2:
            break
        for nw, nv in g[v]:
            if chk[nv]:
                continue
            heappush(pq, (flag*nw, nv))
    return ans

print(prim(-1)**2 - prim(1)**2)