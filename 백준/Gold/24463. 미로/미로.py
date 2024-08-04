import sys
from collections import deque
input=sys.stdin.readline

n, m = map(int, input().split())

lst = [list(input().rstrip()) for _ in range(n)]
se=[]
for i in range(m):
    if lst[0][i] == ".":
        se.append((0,i,1))
for i in range(m):
    if lst[-1][i] == ".":
        se.append((n-1,i,1))
for i in range(1,n-1):
    if lst[i][0]==".":
        se.append((i,0,1))
    if lst[i][-1] == ".":
        se.append((i,m-1,1))
# print(se)
visited=[[0 for _ in range(m)] for _ in range(n)]
q = deque([se[0]])
visited[se[0][0]][se[0][1]] = 1
while q:
    x, y, c = q.popleft()
    if x == se[1][0] and y == se[1][1]:
        break
    for dx, dy in [(1,0),(-1,0),(0,-1),(0,1)]:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and lst[nx][ny]==".":
            visited[nx][ny] = c+1
            q.append((nx,ny,c+1))
# print(*visited,sep='\n')
q = deque([])
q.append((se[1][0],se[1][1],visited[se[1][0]][se[1][1]]))

visited[se[1][0]][se[1][1]]="yes"
while q:
    x, y, c = q.popleft()
    for dx, dy in [(1,0),(-1,0),(0,-1),(0,1)]:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m and visited[nx][ny] == c-1:
            visited[nx][ny] = "yes"
            q.append((nx,ny,c-1))
            break
    
# print(*visited,sep='\n')
for i in range(n):
    for j in range(m):
        if lst[i][j] =="." and visited[i][j] != "yes":
            lst[i][j] = "@"
for i in range(n):
    print("".join(lst[i]))