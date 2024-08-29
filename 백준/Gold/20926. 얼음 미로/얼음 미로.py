import sys
from math import inf
from heapq import heappop, heappush

input = sys.stdin.readline

w, h = map(int, input().split())
lst = [input().rstrip() for _ in range(h)]

for i in range(h):
    for j in range(w):
        if lst[i][j] == "T":
            sx = i
            sy = j
            
        elif lst[i][j] == "E":
            ex = i
            ey = j
def dijk():
    cost = [[inf for _ in range(w)] for _ in range(h)]
    cost[sx][sy] = 0
    pq = [(0,sx,sy)]

    while pq:
        v, x, y = heappop(pq)

        if cost[x][y]<v:
            continue

        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny, nv = x+dx, y+dy, v
            while 0<=nx<h and 0<=ny<w and lst[nx][ny] != "H":
                if lst[nx][ny] == "R":
                    if cost[nx-dx][ny-dy]>nv:
                        heappush(pq,(nv,nx-dx,ny-dy))
                        cost[nx-dx][ny-dy] = nv
                    else:
                        break
                elif lst[nx][ny] == "E":
                    if cost[nx][ny]>nv:
                        heappush(pq,(nv,nx,ny))
                        cost[nx][ny] = nv
                    else:
                        break
                elif lst[nx][ny] == "T":
                    break
                else:
                    nv += int(lst[nx][ny])
                    nx, ny = nx+dx,ny+dy
        
    if cost[ex][ey] == inf:
        print(-1)
    else:
        print(cost[ex][ey])
dijk()
# 이런거 시간 계산 어떻게함???