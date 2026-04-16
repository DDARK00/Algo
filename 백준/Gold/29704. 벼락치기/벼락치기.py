import sys
input=sys.stdin.readline
n, t = map(int, input().split())
dp = [0]*(t+1)
ans = 0
for _ in range(n):
    d, m = map(int, input().split()) # day, money
    ans+=m
    for i in range(t, d-1, -1):
        dp[i]=max(dp[i],dp[i-d]+m)
print(ans-dp[t])