import sys
input = sys.stdin.readline
n, s = map(int, input().split())

lst = list(map(int, input().split()))

pre = 0
l = 0
cnt = 0
ans = 100001
for idx, num in enumerate(lst):
    pre+=num
    cnt+=1
    if pre >= s:
        ans = min(ans, cnt)
    if pre-lst[l]>=s:
        while pre-lst[l]>=s and idx>l:
            pre-=lst[l]
            l+=1
            cnt-=1
        ans = min(cnt, ans)
if ans == 100001:
    print(0)
else:
    print(ans)