import sys
input=sys.stdin.readline

dp=[0]*(100001)
dp[0]=1
dp[1]=1 # 1
dp[2]=2 # 11 2
dp[3]=2 # 111 3 # 홀수 
dp[4]=3 # 1111 121 22 1+2+1+0 # 짝수
dp[5]=3 # 11111 131 212 # 홀수 1 3
dp[6]=6 # 1110111 222 11211 303 # 짝수 0 2 
# dp[7]=6 # 111 1 111 // 12 1 21 // 21 1 12 // 3 1 3 /  / 2 3 2 // 11 3 11

for i in range(7, 100001):
    dp[i]= (dp[i-2]+dp[i-4]+dp[i-6])%1000000009

for _ in range(int(input())):
    print(dp[int(input())])