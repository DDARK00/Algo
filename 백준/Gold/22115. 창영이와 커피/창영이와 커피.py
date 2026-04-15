import sys;input=sys.stdin.readline

n, k = map(int, input().split())
dp=[101]*(100001)
dp[0]=0

coffees = list(map(int, input().split()))
for i in range(n):
    t=coffees[i]
    for j in range(k,t-1,-1):
        dp[j]=min(dp[j],dp[j-t]+1)
    dp[t]=1

print(-1 if dp[k]==101 else dp[k])