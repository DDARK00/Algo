import sys

# import copy

from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

# 세로 가로

uhan = [list(input().split())for _ in range(n)]

covid = []

wall=0

clean =[]

for i in range(n):

    for j in range(m):

        if uhan[i][j] == '0':

            clean.append((i,j))

        elif uhan[i][j] == '1':

            wall+=1

        elif uhan[i][j] == "2":

            covid.append((i,j))

cvcnt = 100

def dfs(k):

    global cvcnt

    

    if k == 3:

        # bfs 

        q = deque([])

        q.extend(covid)

        origin = []

        cnt = 0

        while q:

            vx,vy = q.popleft()

            for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:

                if 0<=vx+dx<n and 0<=vy+dy<m:

                    if uhan[vx+dx][vy+dy] == "0":

                        uhan[vx+dx][vy+dy] = "2"

                        origin.append((vx+dx,vy+dy))

                        q.append((vx+dx,vy+dy))

                        cnt+=1

                        

        cvcnt = min(cnt,cvcnt)

        for i, j in origin:

            uhan[i][j] = "0"

        return

    for i, j in clean:

        if uhan[i][j] == "0":

            uhan[i][j] = "1"

            dfs(k+1)

            uhan[i][j] = "0"

dfs(0)

print(m*n-(cvcnt+len(covid)+wall+3))