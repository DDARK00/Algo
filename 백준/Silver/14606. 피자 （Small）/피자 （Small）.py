# 첫 번째 줄에는 피자판의 개수를 의미하는 양의 정수 N(1 ≤ N ≤ 10) 이 주어진다.

dp = [0] * 11
dp[0] = 0
dp[1] = 0
dp[2] = 1
# dp[3] = 3     dp[2]+dp[1]  1*2
# dp[4] = 6     dp[2]+dp[2]+ 4 2*2
# dp[5] = 10    dp[2]+dp[3]  + 2*3

# dp[8] = 28
n = int(input())
for i in range(3, 11):
    added = 0 if i % 2 == 0 else 1
    dp[i] = dp[i//2] + dp[i//2+added] + (i//2 * (i//2+added))
print(dp[n])
# 아아아아ㅏㅏ아아ㅏ dp인거 알아채기가 너무 힘등ㄹ어~~~~~