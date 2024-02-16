import sys

input = sys.stdin.readline

n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int, input().split())))

# print(tri)

dp = [[0] * (i + 1) for i in range(n)]
# 0-1 1-2 2-3

if n > 1:
    # 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.
    dp[0][0] = tri[0][0]
    dp[1][0] = dp[0][0] + tri[1][0]
    dp[1][1] = dp[0][0] + tri[1][1]
    for i in range(2, n):
        for j in range(i + 1):
            # 2 0 -> 1 0 // 2 1 -> 1 0 or 1 1 자기or 자기-1    2 3 -> 1 2
            if j - 1 >= 0 and j < i:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + tri[i][j]
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + tri[i][j]
            else:
                dp[i][j] = dp[i - 1][j] + tri[i][j]
    # 중에 제일 큰 거
    print(max(dp[n - 1]))
else:
    print(tri[0][0])
