import sys
from math import inf
from collections import deque

input = sys.stdin.readline

n = int(input())

lst = [["." for _ in range(501)] for _ in range(501)]

# 0,0 -> 500,500 501칸?

for _ in range(n):

    x1, y1, x2, y2 = map(int,input().split())

    for i in range(min(x1,x2),max(x1,x2)+1):

        for j in range(min(y1,y2),max(y1,y2)+1):

            lst[i][j] = 1

m = int(input())

for _ in range(m):

    x1, y1, x2, y2 = map(int,input().split())

    for i in range(min(x1,x2),max(x1,x2)+1):

        for j in range(min(y1,y2),max(y1,y2)+1):

            lst[i][j] = "#" # 벽

# lst[0][0] = 2 #visited

visited = [[inf for _ in range(501)] for _ in range(501)]

visited[0][0] = 0

q = deque([(0,0,0)])# x, y, loss hp

# .가능 1데미지 #벽ㄱㄱ

while q:

    x, y, hp = q.popleft()

    # if x ==500 and y == 500:

        

    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:

        nx, ny = x+dx, y+dy

        if 0<=nx<501 and 0<=ny<501 and lst[nx][ny] != "#":

            if lst[nx][ny] == 1 and visited[nx][ny]>hp+1:

                visited[nx][ny] = hp+1

                q.append((nx,ny,hp+1))

            elif lst[nx][ny] == "." and visited[nx][ny] >hp:

                q.appendleft((nx,ny,hp))

                visited[nx][ny] = hp

if visited[500][500] == inf:

    print(-1)

else:

    print(visited[500][500])