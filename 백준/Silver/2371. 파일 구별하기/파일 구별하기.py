import sys
from collections import defaultdict
input=sys.stdin.readline
n=int(input())

files = [input().split() for _ in range(n)]

k=0
unique=[0]*n
cnt=0
while True:
    chk=defaultdict(list)
    for i in range(n):
        if unique[i]:
            continue
        if len(files[i])==k:
            chk[i]=i
            continue
        now=files[i][k]
        chk[now].append(i)
    for val in chk.values():
        if len(val)>1:
            continue
        unique[val[0]]=1
        cnt+=1
    if cnt==n:
        break
    k+=1
print(k+1)