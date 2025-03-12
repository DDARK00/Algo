import sys
input=sys.stdin.readline

r, c = map(int, input().split())

b = [input().rstrip() for _ in range(r)]
visited = [[0]*c for _ in range(r)]

d = [(-1,1), (0, 1), (1, 1)]

ans = 0
def dfs(x, y):
    global ans
    if y == c-1:
        ans+=1
        return True
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if 0<=nx<r and 0<=ny<c and b[nx][ny] == "." and not visited[nx][ny]:
            visited[nx][ny] = 1
            if dfs(nx,ny):
                return True

for i in range(r):
    if b[i][0] == ".":
        dfs(i, 0)
print(ans)