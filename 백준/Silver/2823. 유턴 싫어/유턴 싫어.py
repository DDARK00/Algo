import sys
from collections import deque
input=sys.stdin.readline

r,c=map(int,input().split())
board=[input().rstrip() for _ in range(r)]

cnt=0
for i in range(r):
    for j in range(c):
        if board[i][j]=='.':
            sx,sy=i,j
            cnt+=1

visited=[[0]*c for _ in range(r)]
visited[sx][sy]=1
ok=1

delta=[(1,0,0),(-1,0,1),(0,-1,2),(0,1,3)]
cmd=[(0,2,3),(1,2,3),(0,1,2),(0,1,3),(0,1,2,3)] # 상 하 좌 우 all

q=deque([(sx,sy,4)])
while q:
    x,y,d=q.popleft()
    go=False
    for i in cmd[d]:
        dx, dy, nd = delta[i]
        nx, ny=x+dx, y+dy
        if 0<=nx<r and 0<=ny<c and board[nx][ny]=='.':
            go=True
            if not visited[nx][ny]:
                q.append((nx,ny,nd))
                visited[nx][ny]=1
                ok+=1
    if not go:
        print(1)
        exit()

# print(*visited,sep='\n')
if ok==cnt:
    print(0)
else:
    print(1)