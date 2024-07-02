import sys

from collections import deque

input = sys.stdin.readline

lst = [input().rstrip() for _ in range(8)]

# 7,0 -> 0,7

q = deque([(7,0)])

nxt_q = []

solve = 1

for _ in range(8):

    # 8턴동안 살아남는다면 탈출 가능

    # 구현같네

    visited = [[0]*8 for _ in range(8)]

    while q:

        x, y = q.popleft()

        if lst[x][y] != "#":

            for dx, dy in[(0,0),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1),(0,1),(0,-1)]:

                nx, ny = x+dx, y+dy

                if 0<= nx <8 and 0<= ny <8 and lst[nx][ny] != '#':

                    nxt_q.append((nx,ny))

                    visited[nx][ny] = 1

    if nxt_q:

        q.extend(nxt_q)

        nxt_q = []

        lst.pop()

        lst = ['........']+lst

    else:

        solve = 0

print(solve)