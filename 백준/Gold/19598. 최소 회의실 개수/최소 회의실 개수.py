import sys
from collections import deque
input=sys.stdin.readline

n = int(input())
s = []
e = []
for _ in range(n):
    st, ed = map(int, input().split())
    s.append(st)
    e.append(ed)
s.sort()
e.sort()
use = deque([])
for i in range(n):
    if use and use[0] <= s[i]:
        use.popleft()
    use.append(e[i])
print(len(use))