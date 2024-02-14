import sys

input = sys.stdin.readline

n = int(input())

lst = [[0, 0, 0]]
# 배열
for _ in range(n):
    lst.append(list(map(int, input().split())))

# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

# i<= N-1(i+1) <= N
# r g(이거)            b

dp = [[0] * 3 for _ in range(n + 1)]
# dp= [0] *(n+1)
# 빨강, 초록, 파랑


# dp(i)[0] = min(dpi - 1[1], dpi - 1[2]) + lst[i][0]
# dp(i)[1] = min(dpi - 1[0], dpi - 1[2]) + lst[i][1]
# dp(i)[2] = min(dpi - 1[0], dpi - 1[1]) + lst[i][2]
#
# dp(n)(이게구하려는값) = 012 / 021 / 102 / 120 / 210 / 201

for i in range(1, n+1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + lst[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + lst[i][1]
    dp[i][2] = min(dp[i - 1][1], dp[i - 1][0]) + lst[i][2]

# dp[n][0] = min(lst[n - 1][1] + dp[n - 2][2], lst[n - 1][2] + dp[n - 2][1]) + lst[n][0]
# dp[n][1] = min(lst[n - 1][0] + dp[n - 2][2], lst[n - 1][2] + dp[n - 2][0]) + lst[n][1]
# dp[n][2] = min(lst[n - 1][1] + dp[n - 2][0], lst[n - 1][0] + dp[n - 2][1]) + lst[n][2]
# 조건 더 많은지 알았네... 문제를 읽읍시다;;;

print(min(dp[n]))