import math, sys
input=sys.stdin.readline

n=int(input())
limit=list(sorted(map(int,input().split()),reverse=True))+[0]
m=int(input())

boxs=list(sorted(map(int,input().split()),reverse=True))
if boxs[0]>limit[0]:
    print(-1)
    exit()

bucket=[0]*n
idx=0
for num in boxs:
    if num<=limit[idx+1]:
        idx+=1
    bucket[idx]+=1

ans=bucket[0]
extra=0
bucket_cnt=0

for cnt in bucket:
    extra+=cnt
    bucket_cnt+=1
    ans=max(ans,math.ceil(extra/bucket_cnt))
print(ans)