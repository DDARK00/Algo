import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    r, c, d = map(int,input().split())
    # 행 열 체크포인트
    chk = 0
    maze = [input().rstrip() for _ in range(r)]
    q = deque([])
    visited = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if maze[i][j] == "S":
                q.append((i,j,0))
                visited[i][j] = 1
                break
    
    while chk<=d:
        complete = False
        nq = deque([])
        if chk < d:
            target = str(chk+1)
        else:
            target = 'E'
            complete = True

        find = False # 다음 타겟으로
        while q:
            x, y, cnt = q.popleft()
            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx, ny = x+dx, y+dy

                if 0<=nx<r and 0<=ny<c and maze[nx][ny] != "#" and not visited[nx][ny]:
                    if maze[nx][ny] == target:
                        find = True
                        nq.append((nx,ny,cnt+1))
                        chk+=1
                        break
                    else:
                        visited[nx][ny] = 1
                        q.append((nx,ny,cnt+1))
            if find:
                q = nq
                nq = deque([])
                visited = [[0 for _ in range(c)] for _ in range(r)]
                break

    print(cnt+1)