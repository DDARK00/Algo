import sys
from collections import defaultdict
input=sys.stdin.readline

for _ in range(int(input())):
    lst=input().split()
    n=int(lst[0])
    dd=defaultdict(int)
    for i in range(1,n+1):
        dd[lst[i]]+=1

    # idx, cnt
    ti, tc = sorted(dd.items(), key=lambda x: x[1], reverse=True)[0]
    if tc>n//2:
        print(ti)
    else:
        print("SYJKGW")