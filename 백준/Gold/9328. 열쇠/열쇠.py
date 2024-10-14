import sys

from collections import deque

input=sys.stdin.readline

TC = int(input())

for _ in range(TC):

    h, w = map(int, input().split())

    lst = [input().rstrip() for _ in range(h)]

    

    s = input().rstrip()

    keys = [0]*26

    door = [[] for _ in range(26)]

    if s != "0":

        for c in s:

            keys[ord(c)-97] = 1

    visited = [[0]*w for _ in range(h)]

    

    q = deque([])

    for i in range(w):

        if lst[0][i] != "*":

            q.append((0,i))

        visited[0][i] = 1

        if lst[-1][i] != "*":

            q.append((h-1,i))

        visited[-1][i] = 1

    for i in range(1,h-1):

        if lst[i][0] != "*":

            q.append((i,0))

        visited[i][0] = 1

        if lst[i][-1] != "*":

            q.append((i,w-1))

        visited[i][-1] =1

    answer = 0

    while q:

        x, y = q.popleft() # not *

        t = lst[x][y]

        if t.isupper(): # door

            idx = ord(t)-65

            if not keys[idx]:

                door[idx].append((x, y))

                continue

        elif t.islower():

            idx = ord(t)-97

            if not keys[idx]:

                keys[idx]=1

                q.extend(door[idx])

                door[idx]=[]

        elif t == "$":

            answer+=1

        for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:

            nx, ny = x+dx, y+dy

            if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and lst[nx][ny] != "*":

                visited[nx][ny]=1

                q.append((nx,ny))

    print(answer)

# print(ord("a")) # 97~122 keys

# print(ord("A")) # 65~90 door