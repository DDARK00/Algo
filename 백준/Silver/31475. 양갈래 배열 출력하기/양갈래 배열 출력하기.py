import sys
from collections import deque
input=sys.stdin.readline
n, m = map(int, input().split())
d={'U':0,'L':1,'D':2,'R':3}[input().rstrip()]

if d%2:
    n,m=m,n
board=[[0]*m for _ in range(n)]

mid=m//2
for i in range(n):
    board[n-1-i][mid]=i+1
board[0][mid-1],board[0][mid+1]=n+1,n+1
delta=[(0,-1),(1,0),(0,1),(-1,0)]

order=[0,0,2]
q=deque([(0,mid-1,1),(0,mid+1,-1)])
while q:
    x,y,z=q.popleft()
    dx,dy=delta[order[z]]
    nx,ny=x+dx,y+dy
    if 0<=nx<n and 0<=ny<m and board[nx][ny]==0:
        board[nx][ny]=board[x][y]+1
        q.append((nx,ny,z))
    else:
        order[z]=(order[z]+z+4)%4
        dx,dy=delta[order[z]]
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and board[nx][ny]==0:
            board[nx][ny]=board[x][y]+1
            q.append((nx,ny,z))

if d==0:
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            print(board[i][j],end=' ')
        print()
elif d==1:
    for i in range(m):
        for j in range(n-1,-1,-1):
            print(board[j][i],end=' ')
        print()
elif d==2:
    for i in range(n):
        print(*board[i],sep=' ')
else:
    for i in range(m-1,-1,-1):
        for j in range(n):
            print(board[j][i],end=' ')
        print()