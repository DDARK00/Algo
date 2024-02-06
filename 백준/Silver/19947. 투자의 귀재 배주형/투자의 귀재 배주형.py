money, y = map(int, input().split())

dp = [0] * 12

'''
1년마다 5%의 이율을 얻는 투자 (A)
3년마다 20%의 이율을 얻는 투자 (B)
5년마다 35%의 이율을 얻는 투자 (C)
'''
#
dp[0] = money
# dp[1] = int(money * 1.05)
# dp[2] = int(dp[i - 1] * 1.05))
# dp[3] = max(int(dp[i - 1] * 1.05), int(dp[i - 3] * 1.2))
# # 매번 이율은 소수점 이하를 버림 해서 받는다.
# # ...
# dp[5] = max(int(dp[i - 1] * 1.05), int(dp[i - 5] * 1.35))
#
# case:

# i % 3 == 0
# i % 5 == 0
# i % 3 and i % 5 는 범위가 작구나

# 0 ≤ Y ≤ 10, Y는 정수

for i in range(1, 11):
    max_i = int(dp[i - 1] * 1.05)
    if i // 3 >= 1:
        max_i = max(max_i, int(dp[i - 3] * 1.2))

    if i // 5 >= 1:
        max_i = max(max_i, int(dp[i - 5] * 1.35))

    dp[i] = max_i

print(dp[y])
# 1+3년or 1+1+1+1년  2+3 년 or 5년
