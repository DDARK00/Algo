import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# apps cnt, want

mem = [0] + list(map(int, input().split()))
# spent memory
cost = [0] + list(map(int, input().split()))
# reboot cost

max_range = sum(cost) # 100*100
dp = [[0]*(max_range+1) for _ in range(n+1)]
# idx 1 or 0
# cleaned memory

ans = 10000001
for i in range(1, n+1):
    for j in range(max_range+1):
        if cost[i]>j:
            dp[i][j] = dp[i-1][j] # 0
            continue
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-cost[i]]+mem[i], dp[i-1][j]) # 0 1 0
        if dp[i][j] >= m:
            ans = min(ans, j) # ans vs cost
print(ans)