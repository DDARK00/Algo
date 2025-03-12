import sys
input=sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    m = int(input())
    dp = [0]*(m+1)
    dp[0] = 1
    for coin in lst: # coin
        for money in range(coin, m+1): # money
            dp[money] += dp[money - coin]
    print(dp[m])