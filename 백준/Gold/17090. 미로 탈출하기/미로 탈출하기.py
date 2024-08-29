import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
# 높이 너비

maze = [input().strip() for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

d = dict()
d["U"] = (-1,0)
d["R"] = (0, 1)
d["D"] = (1, 0)
d["L"] = (0,-1)

def dfs(x, y):
    # U인 경우에는 (r-1, c)로 이동해야 한다.
    # R인 경우에는 (r, c+1)로 이동해야 한다.
    # D인 경우에는 (r+1, c)로 이동해야 한다.
    # L인 경우에는 (r, c-1)로 이동해야 한다
    dx, dy = d[maze[x][y]]

    nx = x + dx
    ny = y + dy

    if 0<=nx<n and 0<=ny<m:

        if visited[nx][ny] == -1:

            visited[nx][ny] = 0
            visited[nx][ny] = dfs(nx,ny)
            # return visited[nx][ny]
        # else :
        return visited[nx][ny]

    else :
        return 1

# 일단 0으로 바꾸고 밖으로 나가면 1 주기

ans = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == -1:
        # dfs
            ans += dfs(i,j)

        else:
            ans += visited[i][j]

print(ans)