import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lst = [[0]*n for _ in range(n)]

for _ in range(m):
    x, y, k = map(int, input().split())
    nk = [(-1, 0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    dx, dy = nk[k-1]
    if dx == 0 or dy == 0: # 1 3 5 7
        for i in range(1, n):
            nx, ny = dx*i+x-1, dy*i+y-1
            if 0<= nx <n and 0<=ny<n:
                lst[nx][ny]+=1
    else: #2 4 6 8
        sx, ex = (0, x-1) if dx == -1 else (x, n)
        sy, ey = (0, y-1) if dy == -1 else (y, n)
        for i in range(sx,ex):
            for j in range(sy, ey):
                # print(i, j, x, y)
                lst[i][j] +=1
# print(*lst, sep='\n')
val = 0
for i in range(n):
    for j in range(n):
        if lst[i][j]>val:
            val = lst[i][j]
            ans = (i+1, j+1)
print(*ans)