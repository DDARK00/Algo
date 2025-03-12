import sys
input=sys.stdin.readline

n=int(input())

g = {}
for c in input().split():
    g[c] = 0
for c in input().split():
    g[c] = 1

for c, v in g.items():
    if v == 0:
        print(c)
        break