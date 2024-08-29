import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    n = int(input())

    # n 개의 라인

    lst = [list(map(int,input().split())) for _ in range(2)]

    

    if n ==1:

        print(max(lst[0][0],lst[1][0]))

        continue

    # 1번 고르거나 2번 고르거나 안 고르거나

    dp = [[0,0] for _ in range(n)]

    dp[0] = [lst[0][0], lst[1][0]]

    dp[1] = [dp[0][0]+lst[1][1],dp[0][1]+lst[0][1]]

    # 위 아래 2위0 3아래1

    for i in range(2,n):

        t = max(dp[i-2][0],dp[i-2][1])

        u = dp[i-1][0] # 위

        d = dp[i-1][1] # 아래

        dp[i] = [max(t,u) + lst[i%2][i],max(t,d) + lst[(i+1)%2][i]]

    print(max(dp[n-1]))