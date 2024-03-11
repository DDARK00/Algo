import sys

from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())

# 높이 너비

lst=[input() for _ in range(n)]

visited = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]

q = deque([(0,0,1,True)])

# x y 길이 벽

dis = 100000000

while q:

    x, y, l, drill = q.popleft()

    

    for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:

        nx = x+dx

        ny = y+dy

        if 0<=nx<n and 0<=ny<m:

            if nx == n-1 and ny == m-1:

                dis = l+1

                

                break

            if drill:

                if not visited[nx][ny][0]:

                    visited[nx][ny][0] = 1

                    if lst[nx][ny] == "0":

                        q.append((nx,ny,l+1,drill))

                    else:

                        q.append((nx,ny,l+1,False))

            else:

                # 이미 쓴 경우

                if not visited[nx][ny][1]:

                    visited[nx][ny][1] = 1

                    if lst[nx][ny] == "0":

                        q.append((nx,ny,l+1,drill))

    if dis != 100000000:

        break

# print(visited)

if n-1 ==0 and m-1 ==0:

    print(1)

elif dis == 100000000:

    print(-1)

else:

    print(dis)

# 솔까 직관적으로는 알겠는데 논리적으로 이게 왜 되는지 몰겠당...