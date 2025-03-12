import sys
input=sys.stdin.readline
n, m = map(int, input().split())
 
lst =  [list(map(int, input().split())) for _ in range(n)]
dp = [[[0]*3 for _ in range(m)] for _ in range(n)]
 
for i in range(m):
    dp[0][i] = [lst[0][i]]*3
 
for i in range(n):
    dp[i][0][0] = float('inf')
    dp[i][0][1] = dp[i-1][0][2] + lst[i][0]
    dp[i][0][2] = min(dp[i-1][1][0],
                      dp[i-1][1][1]) + lst[i][0]
    for j in range(1, m-1):
        for k in range(3):
            dp[i][j][k] = min(dp[i-1][j-1+k][(k+1)%3],dp[i-1][j-1+k][(k+2)%3])+ lst[i][j]
    dp[i][m-1][2] = float('inf')
    dp[i][m-1][1] = dp[i-1][m-1][0] + lst[i][m-1]
    dp[i][m-1][0] = min(dp[i-1][m-2][1],dp[i-1][m-2][2])+ lst[i][m-1]
 
# print(*dp,sep='\n')
ans = float('inf')
for l in dp[n-1]:
    ans = min(ans, min(l))
print(ans)