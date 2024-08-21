import sys
from collections import defaultdict

input = sys.stdin.readline

n= int(input())

for _ in range(n):
    d = defaultdict(int)
    s = input().rstrip()
    more = False
    keep = None
    ans = True
    for c in s:
        # print(c,d,more)
        if more :
            if keep == c:
                more = False
                keep = None

                continue
            else:
                ans = False
                break
        d[c]+=1
        if d[c]%3==0:
            more = True
            keep = c
    if more:
        ans = False
    if ans:
        print("OK")
    else:
        print("FAKE")