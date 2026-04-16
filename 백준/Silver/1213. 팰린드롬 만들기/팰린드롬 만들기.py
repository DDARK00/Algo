import sys
from collections import defaultdict
input=sys.stdin.readline

dd=defaultdict(int)
s=input().rstrip()
for c in s:
    dd[c]+=1
odd_ok=False
n=len(s)
if n%2:
    odd_ok=True

answer=[""]*n
i=0
for k in sorted(dd.keys()):
    v=dd[k]
    if v%2:
        if odd_ok:
            odd_ok=False
            answer[n//2]=k
            dd[k]-=1
        else:
            print("I'm Sorry Hansoo")
            exit()
    while dd[k]>0:
        dd[k]-=2
        answer[i]=k
        answer[-1-i]=k
        i+=1
print("".join(answer))