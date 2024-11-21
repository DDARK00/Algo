import sys
from collections import defaultdict
input=sys.stdin.readline

n, m = map(int, input().split())
s = input().rstrip()

g = [0]*26
for c in s:
    g[ord(c)-97]+=1

ans = ""
d = defaultdict(int)
for idx, num in enumerate(g):
    if m>0 and num>0:
        target = min(num, m)
        d[chr(idx+97)]+=target
        m-= target
for c in s:
    if d[c]>0:
        d[c]-=1
    else:
        ans += c
print(ans)