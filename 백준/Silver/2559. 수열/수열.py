import sys
input=sys.stdin.readline

n,k=map(int,input().split())

lst=list(map(int,input().split()))

now=0
for i in range(k):
    now+=lst[i]
answer=now

for i in range(k,n):
    now+=lst[i]
    now-=lst[i-k]
    answer=max(answer,now)

print(answer)