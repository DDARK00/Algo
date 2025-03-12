import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [input().rstrip() for _ in range(n)]

visited = [[[0]*(1<<6) for _ in range(64)] for _ in range(n)]


for i in range(n):
    for j in range(m):
        if maze[i][j] == "0":
            sx, sy = i, j
            break
# 1 2 3 4 5 6
# a b c d e f  - key
# 1 2 4 8 16 32
# A B C D E F  - door

# 64*50*50 160000
q = deque([(sx, sy, 0, 0)])

while q:
    x, y, key, cnt = q.popleft()
    for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m and maze[nx][ny] != "#" and not visited[nx][ny][key]:
            target = maze[nx][ny]
            if target == "1":
                print(cnt+1)
                exit()
            if target.isupper(): # door
                
                if 1&(key>>ord(target)-65):
                    q.append((nx,ny,key,cnt+1))
                    visited[nx][ny][key] = 1
                
            elif target.islower(): # key
                visited[nx][ny][key]=1
                q.append((nx,ny,key|(1<<ord(target)-97),cnt+1))
            else: # .
                visited[nx][ny][key]=1
                q.append((nx, ny, key, cnt+1))
print(-1)