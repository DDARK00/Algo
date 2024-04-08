import sys

from collections import deque

input = sys.stdin.readline

w, h = map(int,input().split())

# 너비 높이

lst = [input().strip() for _ in range(h)]

sted = []

for i in range(h):

    for j in range(w):

        if lst[i][j] == "C":

            sted.append((i,j))

sx = sted[0][0]

sy = sted[0][1]

# 시작점

q = deque([])

delta = [(1,0),[0,1],(-1,0),(0,-1)]

visited = [[[10001]*4 for _ in range(w)] for _ in range(h)]

# print(sx,sy)

for i in range(4):

    visited[sx][sy][i] = 0

    q.append((sx,sy,0,i))

# 시작점은 네방향 -> 방향을 바꾼 횟수

def bfs():

    # 0-1 bfs

    while q:

        x,y,c,d = q.popleft()

        # print(x,y,c,d,"sep")

        for direc in [(d+3)%4,d,(d+1)%4]:

            nx = x + delta[direc][0]

            ny = y + delta[direc][1]

            if 0<=nx<h and 0<=ny<w and lst[nx][ny] != "*":

                if direc == d and visited[nx][ny][direc]>c:

                    # if lst[nx][ny] == "C":

                        # return c

                    visited[nx][ny][direc] = c

                    q.appendleft((nx,ny,c,d))

                    

                elif direc != d and visited[nx][ny][direc]>c+1:

                    # if lst[nx][ny] == "C":

                        # return c+1

                    visited[nx][ny][direc] = c+1

                    q.append((nx,ny,c+1,direc))

bfs()

print(min(visited[sted[1][0]][sted[1][1]]))