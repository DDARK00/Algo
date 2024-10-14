import sys
input = sys.stdin.readline
from collections import deque
from math import inf

n, m, k = map(int, input().split())

q = deque([(0,0,1,False,0)])
# x, y, cnt, day 0 noon / 1 night, wall
lst = [list(map(int,list(input().rstrip()))) for _ in range(n)]

visited = [[[inf]*(k+1) for _ in range(m)] for _ in range(n)]
for i in range(k+1):
    visited[0][0][i] = 1

while q:
    x, y, c, d, w = q.popleft()
    # if visited[x][y][w] < c:
        # continue

    for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
        nx, ny = x+dx, y+dy

        if 0<=nx<n and 0<=ny<m:
            if lst[nx][ny] == 0 and visited[nx][ny][w]>c+1:
                q.append((nx,ny,c+1, not d, w))
                visited[nx][ny][w] = c+1
                
            elif lst[nx][ny] == 1 and w < k: # wall
                if d: # night
                    if visited[nx][ny][w+1]>c+2:
                        q.append((x, y, c+1, not d, w))
                    
                else: # noon 
                    if visited[nx][ny][w+1]>c+1:
                        q.append((nx, ny, c+1, not d, w+1))
                        visited[nx][ny][w+1] = c+1

# print(*visited,sep='\n')
ans = min(visited[n-1][m-1])
if ans == inf:
    print(-1)
else:
    print(ans)