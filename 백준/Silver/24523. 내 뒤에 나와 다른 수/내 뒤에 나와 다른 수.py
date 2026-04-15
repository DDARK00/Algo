import sys
input=sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))

before=lst[0]
idx=0
for i in range(1, n):
    if before==lst[i]:
        continue
    before=lst[i]
    for _ in range(i-idx):
        print(i+1, end=" ")
    idx=i
for _ in range(idx,n):
    print(-1, end=" ")