# 1초 백만(n) 20억
import sys
input=sys.stdin.readline

n, want = map(int, input().split())

lst = list(map(int, input().split()))

s = 1
e = 1000000000
ans = 0
while s<=e:
    m = (s+e)//2
    cut = 0
    for num in lst:
        if num>m:
            cut+=num-m
    if want<=cut:
        ans = m
        s=m+1
    else:
        e=m-1
print(ans)