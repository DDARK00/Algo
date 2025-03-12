import sys
input=sys.stdin.readline

n = int(input())
dp = [0] * max(3, n)
# 갈 수 있는 섬의 수(-1)
dp[0] = 1
dp[1] = 1 # 2
dp[2] = 2 # 23 32
# dp[3] = 3 # 234v 324v 243 [i-1]+[i-3]
# dp[4] = 4 # 2345v 3245v 2435v 2354 [i-1]+[i-3]
# dp[5] = 6 # 23456v 32456v 24356v 23546v 32465 23465  [i-1]+[i-3]

for i in range(3, n):
    dp[i] = (dp[i-1]+dp[i-3])%1000000009
print(dp[n-1])