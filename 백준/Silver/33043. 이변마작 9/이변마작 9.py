import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
g = defaultdict(int)
q = deque([])

ans = 100001
for c in input().split():
    g[c]+=1
    q.append(c)
    if g[c] == 5:
        while q and q[0] != c:
            g[q.popleft()]-=1
        ans = min(len(q), ans)
    elif g[c]>5 :
        while g[c] > 5 or q[0] != c :
            g[q.popleft()]-=1
        ans = min(len(q), ans)

ans = -1 if ans == 100001 else ans

print(ans)