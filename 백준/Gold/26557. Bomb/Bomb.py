import sys
from collections import deque
from math import inf
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    f, r, c = map(int, input().split())
    # 층 높이 너비
    maze = [[input().rstrip() for _ in range(r)]for _ in range(f)]
    # 3 차원 토마토
    find = False

    for layer in range(f):
        for i in range(r):
            for j in range(c):
                if maze[layer][i][j] == "S":
                    sf = layer
                    sx = i
                    sy = j
                    find = True
                    break
            if find:
                break
        if find:
            break

    q = deque([(sf,sx,sy,0)])
    visited = [[[inf for _ in range(c)] for _ in range(r)]for _ in range(f)]
    delta = [(1,0,0), (-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    ans = False

    while q:
        l, x, y,cnt =q.popleft()
        for dl, dx, dy in delta:
            nl, nx, ny = l+dl, x+dx, y+dy
            if 0<=nl<f and 0<=nx<r and 0<=ny<c:
                if maze[nl][nx][ny] == "E":
                    print(cnt)
                    ans = True
                    break

                if visited[nl][nx][ny]>cnt and maze[nl][nx][ny] == '.':
                    visited[nl][nx][ny] = cnt
                    q.appendleft((nl, nx, ny, cnt))

                elif visited[nl][nx][ny]>cnt+1 and maze[nl][nx][ny] == "#":
                    visited[nl][nx][ny] = cnt+1
                    q.append((nl,nx,ny,cnt+1))

        if ans:
            break