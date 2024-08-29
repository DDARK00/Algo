import sys

from collections import deque

n, m = map(int,input().split())

# 높이 너비

visited= [[0]*m for _ in range(n)]

lst = [list(map(int, input().strip())) for _ in range(n)]

# 지도

cnt = 0

boundary = [0]

target = []

for i in range(n):

    for j in range(m):

        if lst[i][j] == 1:

            target.append((i,j))

        elif lst[i][j] == 0 and visited[i][j] == 0:

            # bfs

            q = deque([(i,j)])

            boundary.append(1)

            cnt+=1

            visited[i][j] = cnt

            while q:

                x, y = q.popleft()

                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:

                    nx = x + dx

                    ny = y + dy

                    if 0<= nx < n and 0<=ny<m and lst[nx][ny] == 0 and not visited[nx][ny]:

                        visited[nx][ny] = cnt

                        boundary[cnt] += 1

                        q.append((nx,ny))

            

                    

for x, y in target:

    score = 1

    b_lst = set()

    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:

        if 0<= x+dx < n and 0<=y+dy < m:

            b_lst.add(visited[x+dx][y+dy])

    for i in b_lst:

        score += boundary[i]

    lst[x][y] = score%10

# print(boundary)

# print(visited)

for item in lst:

    print("".join(map(str,item)))

    

    