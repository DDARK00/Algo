import sys
input = sys.stdin.readline

n, l = map(int, input().split())
# 전체수 사용수
lst = list(map(int,input().split()))
k = 0
sums = 0
ans = 0

for idx in range(n):
    sums+= lst[idx]

    if k<l:
        k+=1

    else:
        sums-=lst[idx-l]

    if 129<=sums<=138:
        ans+=1

print(ans)