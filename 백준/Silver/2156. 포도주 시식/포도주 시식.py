import sys

input = sys.stdin.readline

n= int(input())

g=[0]

for _ in range(n):

    g.append(int(input()))

'''

dp[1][0] = 0

dp[1][1] = g[1]

dp[1][2] = g[0]

dp[2][0] = g[1]

dp[2][1] = g[1]+g[2]

dp[2][2] = g[2]

dp[3][0] = g[1]+g[2]

dp[3][1] = g[1]+g[3]

dp[3][2] = g[2]+g[3] max

dp[4][0] = g[1]+g[2]+g[4]

dp[4][1] = g[1]+g[3]+g[4] max

dp[4][2] = g[2]+g[3]

dp[5][0] = g[1]+g[2]+g[4]+g[5]

dp[5][1] = g[1]+g[3]+g[5]

dp[5][2] = g[2]+g[3]+g[5] 

dp[5][3] = g[1]+g[3]+g[4] dpi-1

# 중에서 가장 큰 것

# 나(i)를 골랐을 때. 연속될 때, 안골랐을때

125(6)

1346

235(6)

1245

'''

if n == 1:

    print(g[1])

elif n == 2:

    print(g[1]+g[2])

elif n >=3:

    

    dp=[0 for _ in range(n+1)]

    dp[1] = g[1]

    dp[2] = g[1]+g[2]

    dp[3] = max(dp[2], dp[1]+g[3], g[2]+g[3])

    for i in range(4,n+1):

        dp[i] = max(dp[i-1], dp[i-2]+g[i],dp[i-3]+g[i-1]+g[i])

    # 아니이게뭐라고5시간동안바라만보고있었네~~~~

    print(dp[n])