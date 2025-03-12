import sys
input=sys.stdin.readline
 
dp = [0]*251
dp[0] = 1
dp[1] = 1
dp[2] = 3
# dp[3] = 5
# dp[8] = 171
# 111 12 21
for i in range(3, 251):
    dp[i] = dp[i-1]+dp[i-2]*2
 
s = input()
while s:
    print(dp[int(s)])
    s = input().rstrip()