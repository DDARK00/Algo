import sys

input = sys.stdin.readline

n = int(input().strip())

dp = [(0,0)] *max(n+1,4)

# 횟수와 경로 저장

dp[1] = (0, "1")

dp[2] = (1, "2 1")

dp[3] = (1,"3 1")

for i in range(4,n+1):

    # n-1 n//2 n//3

    m1 = dp[i-1]

    m2 = dp[i//2] if i%2 == 0 else (1000001,"None")

    m3 = dp[i//3] if i%3 == 0 else (1000001,"None")

    route = sorted([m1,m2,m3],key=lambda x :x[0])[0]

    dp[i] = (route[0]+1,f'{i} {route[1]}')

print(dp[n][0])

print(dp[n][1])

# 이런 dp는 환영이야