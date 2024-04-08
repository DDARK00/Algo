import sys
from collections import deque
from math import inf
input= sys.stdin.readline

n = int(input())
lst = [input().strip() for _ in range(n)]
delta = [(1,0),(0,1),(-1,0),(0,-1)]

for i in range(n):
    for j in range(n):
        if lst[i][j] == "#":
            sx = i
            sy = j
            break

visited = [[[inf,inf,inf,inf] for _ in range(n)] for _ in range(n)]
q = deque([])

for i in range(4):
    visited[sx][sy][i] = 0
    q.append((sx,sy,0,i))
    # x y c d

while q:
    x, y, c, d = q.popleft()

    nx = x + delta[d][0]
    ny = y + delta[d][1]
    if 0<=nx<n and 0<=ny<n and lst[nx][ny] != "*" and visited[nx][ny][d]>c:
        if lst[nx][ny] == "#":

            print(c)
            break

        q.appendleft((nx,ny,c,d))
        visited[nx][ny][d] = c

        if lst[nx][ny] == "!":

            q.append((nx,ny,c+1,(d+3)%4))
            q.append((nx,ny,c+1,(d+1)%4))

# print(visited[sted[1][0]][sted[1][1]])