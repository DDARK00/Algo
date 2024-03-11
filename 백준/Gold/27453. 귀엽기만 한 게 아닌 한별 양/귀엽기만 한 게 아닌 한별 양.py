import sys

from collections import deque

input = sys.stdin.readline

n, m, k = map(int,input().split())

# 세로 가로 가드수, k까지는 막는다

# 최근 지나온 3칸

# 학->집

load = [input() for _ in range(n)]

d = [(-1,0),(0,-1),(1,0),(0,1)]

# 상좌하우

sx = sy = None

for i in range(n):

    for j in range(m):

        if load[i][j] == "S":

            sx = i

            sy = j

            break

q = deque([])

visited = [[[0 for _ in range(4)] for _ in range(m)] for _ in range(n)]

dis = 0

for i in range(4):

    nx = sx + d[i][0]

    ny = sy + d[i][1]

    visited[sx][sy][i] = 1

    if 0<=nx<n and 0<=ny<m:

        if load[nx][ny]== "H":

            # H = True

            dis = 1

            break

        elif load[nx][ny]!= "X" and int(load[nx][ny]) <= k:

            q.append((nx,ny,1,0,int(load[nx][ny]),sx,sy))

        

# 시작점xy, 거리, 소지중인 불행123 와진짜어렵다

# 온 길 x  간 길 x

# 방문 배열, 각 상좌하우

# bfs

while q :

    x,y,l, k2, k3,px,py = q.popleft()

    for i in range(4):

        # 4번 돌리는데, 각 기준점에서 상좌하우로 이동

        

        nx = x+d[i][0]

        ny = y+d[i][1]

        if nx == px and ny == py:

            continue

        

        if 0<=nx<n and 0<=ny<m:

            if load[nx][ny] == "H":

                # H = True

                dis = l+1

                break

                

            elif load[nx][ny].isdigit():

                k4 = int(load[nx][ny])

                

                if not visited[x][y][i] and k2+k3+k4<=k:

                    visited[x][y][i]=1

                    # 상0 좌1 하2 우3

                    # -2  -1  0  1

                    # visited[nx][ny][i-2]=1 # 중첩경로박살

                    q.append((nx,ny,l+1,k3,k4,x,y))

    if dis:

        break

                    

# print(visited)

if dis:

    print(dis)

else:

    print(-1)