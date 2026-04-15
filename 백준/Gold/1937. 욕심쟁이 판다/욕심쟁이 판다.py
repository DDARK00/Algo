import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline

def solve():
    global n, forest, dp
    n, forest, dp=None, None, None

    def init():
        global n, forest, dp
        n=int(input())
        forest=[list(map(int, input().split())) for _ in range(n)]
        dp=[[0]*n for _ in range(n)]
        return

    def dfs(x,y): # 좌표, 크기, 양
        if dp[x][y]!=0:
            return dp[x][y]
        rst=0
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and forest[nx][ny]>forest[x][y]:
                rst=max(rst,dfs(nx,ny))
        rst+=1
        dp[x][y]=rst
        return rst

    def p_out(answer):
        # for k in dp:
            # print(*k)
        print(answer)
        return

    init()
    answer=0
    for i in range(n):
        for j in range(n):
            if dp[i][j]==0:
                dfs(i,j)
                answer=max(answer,dp[i][j])

    p_out(answer)
    return 0

solve()