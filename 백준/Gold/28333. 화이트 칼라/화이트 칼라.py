import sys
from collections import deque, defaultdict
input=sys.stdin.readline

def solve(n,m):
    # init
    g=defaultdict(list)
    for _ in range(m):
        a,b=map(int,input().split())
        g[a].append(b)

    # 1->n
    q=deque([(1,0)])
    visited=[float('inf')]*(n+1)
    visited[1]=0
    p_v=[[] for _ in range(n+1)]

    # bfs
    while q:
        v,c=q.popleft()
        for nv in g[v]:
            if visited[nv]>c+1:
                q.append((nv,c+1))
                visited[nv]=c+1
                p_v[nv].append(v)
            elif visited[nv]==c+1:
                p_v[nv].append(v)

    # trace
    answer=set()
    answer.add(1)
    answer.add(n)
    target=n
    q=deque([n])
    while q:
        v=q.popleft()
        for nv in p_v[v]:
            if nv not in answer:
                answer.add(nv)
                q.append(nv)

    # print
    print(*sorted(list(answer)))

# t
for _ in range(int(input())):
    n,m=map(int,input().split())
    solve(n,m)