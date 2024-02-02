n, k = map(int, input().split())

# n번째 행의 k번째 숫자
# 이 때, 1 ≤ k ≤ n ≤ 30을 만족한다.
dp = [0] * 31
dp[0] = 0
dp[1] = [1]
dp[2] = [1, 1]
dp[3] = [1, 2, 1]

if n <= 3:
    print(dp[n][k - 1])
else:

    #
    # dp[4] = [1, 3, 3, 1]
    # dp[5] = [1, 4, 6, 4, 1]

    # n-2 번을 계산하고 앞 뒤를 1로 감싼다
    # 이렇게 하는게 맞냐...??? 아니진짜모르겠는데???

    for i in range(4, n + 1):
        t_ar = [1]
        for z in range(i - 2):
            t_ar.append(dp[i - 1][z] + dp[i - 1][z + 1])
        t_ar.append(1)
        dp[i] = t_ar

    print(dp[n][k - 1])
