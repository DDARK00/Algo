import sys

from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

lst = [input().split() for _ in range(n)]

q = deque([(0,0)])

lst[0][0] = 1

delta = [(0,1),(0,-1),(1,0),(-1,0)]

def air(flag):

    while q:

        x,y = q.popleft()

        if flag:

            lst[x][y] = 1

        for dx, dy in delta:

            nx, ny = x+dx, y+dy

            if 0<=nx<n and 0<=ny<m and lst[nx][ny] == "0":

                lst[nx][ny] = 1

                q.append((nx,ny))

air(0)

ans = 0

while True:

    change_cnt = 0

    for i in range(n):

        for j in range(m):

            if lst[i][j] == "1":

                cnt = 0

                for dx,dy in delta:

                    nx, ny = i+dx, j+dy

                    if lst[nx][ny] == 1:

                        cnt+=1

                if cnt >= 2 :

                    lst[i][j] = "0"

                    q.append((i,j))

                    change_cnt+=1

    if change_cnt>0:

        ans+=1

        air(1)

    else:

        break

print(ans)

# print(*lst,sep="\n")