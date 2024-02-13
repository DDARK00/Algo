import sys

from collections import deque

# n줄 m개씩

n,m = map(int, input().split())

g = [list(map(int,input().split())) for _ in range(n)]

# print(g)

start =[]

visited = [[-1]*m for _ in range(n)]

# 입력에서 2는 단 한개이다.

for i in range(n):

    for j in range(m):

        if g[i][j] == 2:

            start.append((i, j))

            visited[i][j] = 0

            break

di = [0, 1, 0, -1]

dj = [1, 0, -1, 0]

# bfs

q = deque(start)

# 2나 1이면 go

while q:

    i, j = q.popleft()

    val = visited[i][j]

    if g[i][j] > 0:

        for k in range(4):

            dxi = i + di[k]

            dxj = j + dj[k]

            if 0 <= dxi < n and 0 <= dxj < m:

                if g[dxi][dxj] == 1 and visited[dxi][dxj] == -1:

                    visited[dxi][dxj] = val +1

                    q.append((dxi, dxj))

# 그래프 방문 시작탐색 bfs 출력

i = 0

j = 0

while i < n:

    while j < m:

        if visited[i][j] >=0:

            print(visited[i][j], end = " ")

        elif visited[i][j] == -1 and g[i][j] == 0:

            print(0 , end=" ")

        else:

            print(-1, end=" ")

        j+=1

    i+=1

    j=0

    print()