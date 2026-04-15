import sys
input=sys.stdin.readline

def solve(n,m):
    board=[list(input().rstrip()) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j]=='.':
                board[i][j]=0

    for i in range(n):
        for j in range(m):
            if board[i][j]=='.':
                board[i][j]=0
            elif board[i][j]=='*':
                for nx, ny in [(i+1,j),(i-1,j),(i,j+1),(i,j-1),(i+1,j-1),(i+1,j+1),(i-1,j-1),(i-1,j+1)]:
                    if 0<=nx<n and 0<=ny<m:
                        if board[nx][ny]!='*':
                            board[nx][ny]+=1

    for l in board:
        print(*l,sep='')

while True:
    r,c=map(int,input().split())
    if r==0 and c==0:
        break
    solve(r,c)