import sys
from collections import defaultdict
input=sys.stdin.readline

n, m=map(int,input().split())
dd=defaultdict(int)
for _ in range(n):
    for k in map(int,input().split()):
        dd[k]+=1
rst=[0,0]
for v in dd.values():
    rst[v%2]+=1

# even odd
if m%2==0 and rst[1]:
    print("NO")
else: # m odd
    if rst[1]<=n:
        print("YES")
    else:
        print("NO")