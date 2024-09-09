import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int,input().split())

#세로 가로

doro = [list(map(int,input().split())) for _ in range(n)]

endx, endy = n-1,m-1

def dfs(x,y):

    if x==endx and y == endy:

        return 1

        

    if visited[x][y]>-1:

        return visited[x][y]

    

    now = doro[x][y]

    cnt = 0

    for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:

        nx = x+dx

        ny = y+dy

        

        if 0<=nx<n and 0<=ny<m and doro[x][y]>doro[nx][ny]:

            cnt += dfs(nx,ny)

    visited[x][y] =cnt

    return cnt

visited = [[-1 for _ in range(m)]for _ in range(n)]

dfs(0,0)

# print(*visited, sep="\n")

print(visited[0][0])

# 너무어려웡

# visited-1로 초기화하면 0이상일때 이미 탐색한 곳

# cnt가 0이 나올 수 있어서

# visited 0초기화면 구분불가