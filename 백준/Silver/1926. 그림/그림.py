import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

lst = [input().split() for _ in range(n)]
m_size = 0
ans = 0

for i in range(n):
    for j in range(m):
        if lst[i][j] == "1":
            lst[i][j] = 0
            ans+=1
            q = deque([(i,j)])
            cnt = 1
            while q:
                x, y= q.popleft()
                for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx, ny = x+dx, y+dy
                    if 0<= nx < n and 0<=ny<m and lst[nx][ny] == "1":
                        lst[nx][ny] = 0
                        q.append((nx, ny))
                        cnt+=1
            m_size = max(m_size,cnt)
                        
print(ans)
print(m_size)