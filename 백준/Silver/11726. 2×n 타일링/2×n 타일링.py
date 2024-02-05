# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
n = int(input())

dp=[0]*1001
dp[1]=1
dp[2]=2
for i in range(3, 1001):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[n]%10007)
# 2 3 5 8 13 21 34 55