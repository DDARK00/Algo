import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())

d = defaultdict(int)
for _ in range(n):
    a, b, c = map(int, input().split())
    # a<b<c
    if d[a] or d[b] or d[c]:
        print(1)
        exit()
    d[a] = 1
    d[b] = 1
    d[c] = 1
print(0)