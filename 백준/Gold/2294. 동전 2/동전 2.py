import sys
input=sys.stdin.readline
n, k=map(int,input().split())

dp=[100001]*(k+1)
dp[0]=0
for _ in range(n):
    v=int(input())
    for i in range(v,k+1):
        dp[i]=min(dp[i-v]+1,dp[i])

print(-1 if dp[k]==100001 else dp[k])