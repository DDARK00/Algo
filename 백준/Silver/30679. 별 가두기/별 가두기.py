import sys
input=sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[[-1]*4 for _ in range(m)] for _ in range(n)]
ans = [0]*n # 0out 1in

delta = [(0,1),(1,0),(0,-1),(-1,0)]
for i in range(n):
    st = [(i,0, 0)]
    visited[i][0][0] = i
    while st:
        x, y, d = st.pop()
        w = grid[x][y]
        nx, ny = x+delta[d][0]*w, y+delta[d][1]*w
        if 0<=nx<n and 0<=ny<m:
            if visited[nx][ny][d] == -1:
                visited[nx][ny][d] = i
                st.append((nx, ny, (d+1)%4))
            elif visited[nx][ny][d] == i:
                ans[i] = 1
            else:
                ans[i] = ans[visited[nx][ny][d]]
cnt = 0
nums = ""
for idx, num in enumerate(ans):
    cnt+=num
    nums += f"{idx+1} " if num else ""
if cnt>0:
    print(cnt, nums, sep="\n")
else:
    print(0)