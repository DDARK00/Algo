import sys
n, k = map(int, input().split())

lst = list(map(int, input().split()))
ans=0
for i in range(n//2):
    a, b = lst[i], lst[-1-i]
    a, b = min(a, b), max(a, b)
    t = (b-a)//k
    ans +=t
    a += t*k
    ans += min(b-a, (a+k-b)+1)
    
print(ans)