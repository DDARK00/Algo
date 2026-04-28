import sys
input=sys.stdin.readline
n=int(input())
# t=0 start
lst=[tuple(map(int,input().split())) for _ in range(n)] # need, deadline
lst.sort(key=lambda x:-x[1])
# print(lst)
before=lst[0][1]
for need, dead in lst:
    if before<dead:
        before-=need
    else:
        before=dead-need

if before<0:
    print(-1)
else:
    print(before)