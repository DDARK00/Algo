import sys
input=sys.stdin.readline

n,m=map(int,input().split())
lst=[0]+list(map(int,input().split()))
# 거리 시간
dp=[[0]*(n+2) for _ in range(m+1)]
# dp[시간][거리] dp가아니라 완탐인데?
dp[0][0]=1
for i in range(m):
    for j in range(n,-1,-1):
        if dp[i][j]!=0: # 1칸 or 2칸
            if j+1<n+1: # 1칸
                k=lst[j+1]
                dp[i+1][j+1]=max(dp[i+1][j+1],dp[i][j]+k)
            if j+2<n+1: # 2칸
                k=lst[j+2]
                dp[i+1][j+2]=max(dp[i+1][j+2],dp[i][j]//2+k)
ans=0
for i in range(m+1):
    ans=max(ans,max(dp[i]))
print(ans)