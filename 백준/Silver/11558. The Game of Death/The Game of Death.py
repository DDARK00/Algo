import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    lst = [0]+[int(input()) for _ in range(n)]

    visited = [0]*(n+1)
    q  = deque([(1,0)]) # cnt idx
    while q:
        v, cnt = q.popleft()
        if v == n:
            print(cnt)
            break
        if not visited[v]:
            visited[v]=1
            q.append((lst[v],cnt+1))
        else:
            print(0)
            break