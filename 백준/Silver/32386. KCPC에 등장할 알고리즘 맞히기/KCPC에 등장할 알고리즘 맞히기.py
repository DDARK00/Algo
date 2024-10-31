import sys
from collections import defaultdict
input=sys.stdin.readline

g = defaultdict(int)
n = int(input())
for _ in range(n):
    _, _, *tag = input().split()
    for t in tag:
        g[t]+=1

k = sorted(g, key=lambda x:g[x], reverse=True)

if len(k) == 1 or g[k[0]] != g[k[1]]:
    print(k[0])
else:
    print(-1)