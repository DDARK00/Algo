import sys
input = sys.stdin.readline

n = int(input())

lst = [list(input().rstrip()) for _ in range(n)]

ans = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if lst[i][j] != ".":
            for dx, dy in [(0,1),(0,-1),(1,0),(1,-1),(1,1),(-1,0),(-1,-1),(-1,1)]:
                nx, ny = i+ dx, j + dy
                if 0<= nx < n and 0<= ny < n and ans[nx][ny] not in ["*","M"]:
                    v = ans[nx][ny]+int(lst[i][j])
                    ans[nx][ny] = v if v<10 else "M"
            ans[i][j] = "*"
for i in range(n):
    print(*ans[i],sep="")