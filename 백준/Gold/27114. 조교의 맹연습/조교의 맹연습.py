import sys
input=sys.stdin.readline
a,b,c,k=map(int,input().split())
# -1 +1 +2 -> 0

dp=[[1000001]*(4) for _ in range(k+1)]
dp[0][0]=0
for i in range(min([a,b,c]),k+1):
    for p,q in [(a,3),(b,1),(c,2)]:
        if i-p>=0:
            for j in range(4):
                dir=(q+j)%4
                dp[i][j]=min(dp[i][j],dp[i-p][dir]+1)
ans=dp[k][0]
if ans==1000001:
    ans=-1
print(ans)