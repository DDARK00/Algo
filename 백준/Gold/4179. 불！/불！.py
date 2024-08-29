import sys

from collections import deque

input = sys.stdin.readline

r, c = map(int,input().split())

lst = [input().strip() for _ in range(r)]

visited = [[10000001]*c for _ in range(r)]

visit = [[0]*c for _ in range(r)]

bul=deque([])

ji = deque([])

for i in range(r):

    for j in range(c):

        if lst[i][j] == "F":

            bul.append((i,j,0))

            visited[i][j] = 0

        elif lst[i][j] == "J":

            ji.append((i,j,0))

            visit[i][j] = 1

delta = [(0,1),(1,0),(0,-1),(-1,0)]

# bfs

while bul:

    x, y, k = bul.popleft()

    for dx, dy in delta:

        nx,ny = x+dx, y+dy

        if 0<= nx < r and 0<= ny < c:

            if lst[nx][ny] !="#" and visited[nx][ny]>k+1:

                visited[nx][ny] = k+1

                bul.append((nx,ny,k+1))

flag = False

ans = None

while ji:

    x,y,k = ji.popleft()

    for dx, dy in delta:

        nx, ny = x+dx, y+dy

        if 0<=nx<r and 0<=ny<c:

            if lst[nx][ny] !="#" and visited[nx][ny]>k+1 and not visit[nx][ny]:

                visit[nx][ny] = 1

                ji.append((nx,ny,k+1))

        else:

            flag = True

            ans = k+1

            break

    if flag:

        break

#print(flag,ans)

#print(*visit, sep="\n")

#print(*visited, sep="\n")

if flag:

    print(ans)

else:

    print("IMPOSSIBLE")