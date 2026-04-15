import sys
input=sys.stdin.readline

n, m, h = map(int, input().split())
# 학생 블록 높이
dp = [[0]*(100001) for _ in range(51)]
dp[0][0]=1

for i in range(1, n+1): # 사람 
    blocks = list(map(int, input().split()))
    for j in range(h,-1,-1): # 높이
        dp[i][j]=dp[i-1][j]
        for block in blocks: # 현재 블럭
            if block > j : continue
            dp[i][j]=(dp[i][j]+dp[i-1][j-block])%10007
print(dp[n][h])