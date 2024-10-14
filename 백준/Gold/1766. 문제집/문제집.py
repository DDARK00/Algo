import sys
from heapq import heappop, heappush
input=sys.stdin.readline

n, m = map(int, input().split())
waiting = [[] for _ in range(n+1)]

chk = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    # a -> b
    waiting[a].append(b)
    chk[b]+=1

pq = []
ans = []
for i in range(1,n+1):
    if chk[i] == 0:
        heappush(pq, i)
    # 앞 문제부터

while pq: #  큐에 있다-> 풀 수 있다
    solve = heappop(pq)
    ans.append(solve)
    for nxt in waiting[solve]:
        chk[nxt]-=1
        if chk[nxt] == 0:
            heappush(pq, nxt)
    
print(*ans)