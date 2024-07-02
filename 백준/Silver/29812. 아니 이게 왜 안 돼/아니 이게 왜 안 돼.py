import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
s = input().rstrip()
d, m = map(int,input().split())

dc = defaultdict(int)
cnt = 0
energy = 0
for c in s:
    if c not in ["H","Y","U"]:
        cnt +=1
    else:
        energy += min(d*cnt,m+d)
        cnt = 0
        dc[c]+=1

energy += 0 if cnt==0 else min(d*cnt,m+d)
ans = min(dc["H"],dc["Y"],dc["U"])
if energy == 0:
    energy ="Nalmeok"
if ans == 0:
    ans = "I love HanYang University"
print(energy)
print(ans)