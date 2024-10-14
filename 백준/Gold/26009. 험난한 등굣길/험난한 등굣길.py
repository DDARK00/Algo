import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

k = int(input())

visited = [[0 for _ in range(m)] for _ in range(n)]


for _ in range(k):
    r, c, d = map(int, input().split())
    r-=1
    c-=1
    d+=1
    # rc를 중심으로 d만큼 좌표
    # 상하좌우
    visited[r][c]=1
    for i in range(d):
        for dx, dy in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            nx = dx*(i)+r
            ny = dy*(d-i-1)+c
            if 0<=nx<n and 0<=ny<m:
                visited[nx][ny]=1
q = deque([(0,0,1)])
# print(*visited, sep='\n')
while q:
    x, y, c = q.popleft()
    for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
        nx, ny = x+dx, y+dy
        if nx==n-1 and ny==m-1:
            print("YES")
            print(c)
            exit()
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            visited[nx][ny]=1
            q.append((nx, ny, c+1))
print("NO")