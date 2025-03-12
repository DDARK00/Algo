import sys
from collections import deque
input = sys.stdin.readline

for t in range(1, int(input())+1):
    r, c = map(int, input().split())
    maze = [list(input().rstrip()) for _ in range(r)]
    sxsy =False
    for i in range(r):
        for j in range(c):
            if maze[i][j] == "S":
                maze[i][j] = "X"
                sx, sy = i, j
                sxsy = True
                break
        if sxsy:
            break

    q = deque([(sx, sy, 0)])
    find = False
    while q:
        x, y, cnt = q.popleft()
        for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx, ny = dx+x,y+dy
            if 0<=nx<r and 0<=ny<c and maze[nx][ny] != "X":
                if maze[nx][ny] in ["O", "0"]:
                    q.append((nx, ny, cnt+1))
                    maze[nx][ny] = "X"
                else:
                    find=True
                    print("Shortest Path:",cnt+1)
                    break
        if find:
            break
    if not find:
        print("No Exit")