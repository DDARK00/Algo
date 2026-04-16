import sys
from collections import defaultdict
input=sys.stdin.readline
xa=defaultdict(int)
ya=defaultdict(int)
for _ in range(int(input())):
    x,y=map(int,input().split())
    xa[x]+=1
    ya[y]+=1
ans=0
for k,v in xa.items():
    ans+=v>=2
for k,v in ya.items():
    ans+=v>=2
print(ans)