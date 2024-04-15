import sys
from collections import deque

input = sys.stdin.readline

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    # r*c 행렬이 l개
    # l층 r높이 c너비
    maps = []
    for _ in range(l):
        maps.append([input().rstrip() for _ in range(r)])
        input()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if maps[i][j][k] == "S":
                    sx = i  # 높이
                    sy = j  # 너비
                    sz = k  # 층
                    break
                # elif maps[i][j][k] == "E":
                #     ex = i  # 높이
                #     ey = j  # 너비
                #     ez = k  # 층

    q = deque([(sx, sy, sz, 0)])
    visited = [[[0] * c for _ in range(r)] for _ in range(l)]
    visited[sx][sy][sz] = 1
    ans = -1
    while q:
        x, y, z, cnt = q.popleft()
        if maps[x][y][z] == "E":
            ans = cnt
            break
        for dx, dy, dz in [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0),
                           (-1, 0, 0)]:  # 인접한 6개의 칸(동,서,남,북,상,하)
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c and maps[nx][ny][nz] != "#" and not visited[nx][ny][nz]:
                visited[nx][ny][nz] = 1
                q.append((nx, ny, nz, cnt + 1))

    if ans == -1:
        print('Trapped!')
    else:
        print(f'Escaped in {ans} minute(s).')
