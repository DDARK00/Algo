import sys
input = sys.stdin.readline

# 기본 접근법 : dp를 이용한 현재아이템 넣기안넣기
n, k = map(int,input().split())
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1,n+1):
    w, v =map(int,input().split())
    # 무게 가치
    # 최대 k
    for j in range(1,k+1):
        if w<=j:# 무게제한
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)

        else:
            dp[i][j] = dp[i-1][j]
print(max(dp[n]))