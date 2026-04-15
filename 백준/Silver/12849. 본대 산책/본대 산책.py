g=[[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4, 5], [2, 3, 5, 6], [3, 4, 7], [4, 7], [5, 6]]
dp=[[0]*8 for _ in range(100001)]
dp[0][0]=1
n=int(input())
# t=i 일 때 노드 j에 방문하는 수
for i in range(1,n+1):
    for j in range(8):
        cnt=0
        for k in g[j]:
            cnt+=dp[i-1][k]
            cnt%=1000000007
        dp[i][j]=cnt
print(dp[n][0])