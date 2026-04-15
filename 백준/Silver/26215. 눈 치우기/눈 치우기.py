import sys
input=sys.stdin.readline
n=int(input())
lst=list(map(int,input().split()))
answer=0
if max(lst)>1440:
    print(-1)
    exit()
l=0
while l<n-1:
    lst.sort()
    if lst[l]==0:
        l+=1
        continue
    lst[l]-=1
    lst[-1]-=1
    answer+=1

answer+=lst[l]
if answer>1440:
    print(-1)
else:
    print(answer)