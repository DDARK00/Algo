import sys

from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

# 높이 너비

maze = [input().strip() for _ in range(n)]

exits = []

for i in range(n):

    for j in range(m):

        if maze[i][j] == "#":

            exits.append((i,j,0))

m_people = 0

# bfs

for exit in exits:

    q = deque([exit])

    visited = [[0 for _ in range(m)]for _ in range(n)]

    m_cnt = 100001

    people = 0

    Han = False

    while q:

        x, y, c = q.popleft()

        for dx, dy in [(1,0),(-1,0),(0,-1),(0,1)]:

            nx = x+dx

            ny = y+dy

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maze[nx][ny] != "X":

                if c+1 > m_cnt:

                    break

                if maze[nx][ny] == "P":

                    people +=1

                elif maze[nx][ny] == "H":

                    Han = True

                    m_cnt = c+1

                visited[nx][ny] =1

                q.append((nx, ny, c+1))

    if Han:

        m_people = max(m_people, people)

print(m_people)