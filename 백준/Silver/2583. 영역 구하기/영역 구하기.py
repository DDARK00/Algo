import sys

sys.setrecursionlimit(10**6)

input=sys.stdin.readline

m, n, k = map(int,input().split())

lst = [[0]*n for _ in range(m)]

for _ in range(k):

    a,b,c,d = map(int,input().split())

    for i in range(b,d):

        for j in range(a,c):

            lst[i][j] = 1

maps= 0

c = []

for i in range(m):

    for j in range(n):

        if lst[i][j] == 0:

            maps+=1

            lst[i][j] = 1

            st = [(i,j)]

            cnt = 1

            while st:

                x, y = st.pop()

                for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:

                    nx, ny = x+dx, y+dy

                    if 0<=nx<m and 0<=ny<n and lst[nx][ny] == 0:

                        lst[nx][ny] = 1

                        cnt+=1

                        st.append((nx,ny))

            c.append(cnt)

print(maps)

c.sort()

print(*c)