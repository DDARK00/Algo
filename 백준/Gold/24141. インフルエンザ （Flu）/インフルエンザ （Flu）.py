import sys, math
from collections import deque
input=sys.stdin.readline

n = int(input()) # citys
m = int(input()) # virus survive
d = int(input()) # range
k = int(input()) # after k days

sx, sy = map(int, input().split())

city = [[-1]*1000 for _ in range(1000)]
# city[sx][sy] = 0 # visit

for _ in range(n-1):
    a, b = map(int, input().split())
    city[a][b] = -2 # city


delay_q = [(sx, sy)] # x, y
nxtq =[]

ans = [0]*(k+1)
ans[0] = 1

day = 0

def get_dist(x1,x2,y1,y2):
    return math.sqrt(((x1 - x2) ** 2 + (y1 - y2) ** 2))

def bfs():
    for ox, oy in delay_q:
        q = deque([(ox,oy)])
        city[ox][oy] = (ox,oy)
        while q:
            x, y = q.popleft()
            for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                nx, ny = x+dx, y+dy
                if 0<=nx<1000 and 0<=ny<1000 and city[nx][ny] != (ox,oy) :
                    dist = get_dist(ox,nx,oy,ny)
                    if dist > d:
                        continue
                    if city[nx][ny] == -2 :
                        nxtq.append((nx,ny))
                    city[nx][ny] = (ox,oy)
                    q.append((nx,ny))

while True:
    if k == day:
        break

    bfs()
    # print(nxtq)
    if nxtq:
        day+=1
        delay_q = nxtq[:]
        ans[day] = len(nxtq)
        nxtq = []
    else:
        break
# print(ans)
# print(sum(ans))
# print(sum(ans[:11]))
print(sum(ans[k-m+1:k+1]))