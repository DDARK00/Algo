import sys

from math import inf

from heapq import heappop, heappush

input = sys.stdin.readline

n, m = map(int,input().split())

lst = [list(input().rstrip()) for _ in range(n)]

start = -1,-1

for i in range(n):

    for j in range(m):

        if lst[i][j] =='g':

            for dx, dy in[(0,1),(0,-1),(1,0),(-1,0)]:

                ni,nj = i+dx,j+dy

                if 0<=ni<n and 0<=nj<m and lst[ni][nj] =='.':

                    lst[ni][nj] = 1

        elif lst[i][j] == "S":

            start = i, j

cost = [[[inf,inf] for _ in range(m)] for _ in range(n)]

cost[start[0]][start[1]] = [0,0]

# 쓰레기 통과, 쓰레기 옆 통과

# 1순위 쓰레기 거르기 2순위 쓰레기옆 거르기?

#dijk

pq = [(0,0,*start)]

# print(*lst,sep="\n")

while pq:

    ga, du, x, y = heappop(pq)

    if cost[x][y][0]< ga:

        continue

    for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:

        nx, ny = x+dx, y+dy

        if 0<=nx<n and 0<=ny<m:

            if lst[nx][ny] == "g" and cost[nx][ny][0]> ga+1:

                cost[nx][ny]=[ga+1,du]

                heappush(pq,(ga+1,du,nx,ny))

            elif lst[nx][ny] == 1 and cost[nx][ny][0]>=ga and cost[nx][ny][1] > du+1:

                cost[nx][ny] = [ga,du+1]

                heappush(pq,(ga,du+1,nx,ny))

            elif lst[nx][ny] == "." and cost[nx][ny][0]>ga:

                cost[nx][ny] = [ga,du]

                heappush(pq,(ga,du,nx,ny))

            elif lst[nx][ny] == "F":

                print(ga,du)

                exit()

# print(*cost,sep="\n")