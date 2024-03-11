import sys

from collections import deque

input = sys.stdin.readline

n = int(input())

# n * n

lst = [list(map(int,input().split()))for _ in range(n)]

m_level = max(map(max,lst))

# print(m_level)

# 높이는 1이상 100 이하

max_land = 1

for level in range(1, m_level):

    land_cnt = 0

    visited =[[0 for _ in range(n)] for _ in range(n)]

    # 이걸 100번 돌면 시간 안 터지나...?

    # print(level)

    

    for i in range(n):

        for j in range(n):

            

            #bfs

            if lst[i][j] > level and not visited[i][j]:

                q = deque([(i,j)])

                visited[i][j] = 1

                land_cnt += 1

                

                

                while q:

                    x, y = q.popleft()

                    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:

                        if 0<= x+dx<n and 0<=y+dy<n and not visited[x+dx][y+dy] and lst[x+dx][y+dy] > level:

                            visited[x+dx][y+dy]=1

                            q.append((x+dx,y+dy))

                            

                

    max_land = max(land_cnt, max_land)

    

print(max_land)

                            

                    

            

        