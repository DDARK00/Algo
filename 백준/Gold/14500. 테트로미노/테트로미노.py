import sys

input = sys.stdin.readline

n, m = map(int,input().split())

# 가로 세로

# 4칸의 합

lst = [list(map(int,input().split())) for _ in range(n)]

max_v = max(map(max,lst))

delta = [(0,1),(1,0),(-1,0),(0,-1)]

visited = [[0]*m for _ in range(n)]

found = 0

def calc(x,y,sub,depth):

    global found

    

    if depth ==4:

        # print(i,j,found)

        found = max(found,sub)

        return

    if found > sub+(4-depth)*max_v:

        # print(found,sub,3-depth,max_v)

        return

    for dx, dy in delta:

        nx = x+dx

        ny = y+dy

        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:

            visited[nx][ny]= 1

            calc(nx,ny,sub+lst[nx][ny],depth+1)

            visited[nx][ny]=0

def tspin(x,y,sub):

    global found

    cn = []

    for dx, dy in delta:

        nx = x+dx

        ny = y+dy

        if 0<=nx<n and 0<=ny<m:

            cn.append(lst[nx][ny])

    if len(cn)>2:

        cn.sort()

        # print(cn, x,y)

        found = max(found,cn[-1]+cn[-2]+cn[-3]+sub)

    

    

for i in range(n):

    for j in range(m):

        visited[i][j]=1

        calc(i,j,lst[i][j],1)

        tspin(i,j,lst[i][j])

        visited[i][j]=0

print(found)