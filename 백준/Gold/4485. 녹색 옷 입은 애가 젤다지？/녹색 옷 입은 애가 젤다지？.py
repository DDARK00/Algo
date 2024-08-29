import sys

from math import inf

from heapq import heappop, heappush

input = sys.stdin.readline

def dijk():

    pq = [(lst[0][0],0,0)] # weight, x, y 

    visited[0][0] = lst[0][0]

    while pq:

        w, x, y = heappop(pq)

        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:

            nx = x + dx

            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] > w + lst[nx][ny]:

                visited[nx][ny] = w + lst[nx][ny]

                heappush(pq,(w + lst[nx][ny], nx, ny))

tc = 1

while True:

    n = int(input())

    if n == 0:

        break

    lst = [list(map(int,input().split())) for _ in range(n)]

    # 0,0 -> n-1,n-1

    

    visited = [[inf]*n for _ in range(n)]

    dijk()

    print(f'Problem {tc}: {visited[n-1][n-1]}')

    tc+=1