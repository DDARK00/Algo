import sys

from collections import deque

input = sys.stdin.readline

n = int(input())

# n*n

danzi = []

d = [(1,0),(0,1),(-1,0),(0,-1)]

for _ in range(n):

    danzi.append(list(input()))

q = deque([])

all_d = 0

d_lst = []

for i in range(n):

    for j in range(n):

        if danzi[i][j] == '1':

            q.append((i,j))

            danzi[i][j]='0'

            d_cnt =1

            all_d +=1

            while q:

                x, y = q.popleft()

                for dx,dy in d:

                    if 0<=x+dx<n and 0<=y+dy<n:

                        if danzi[x+dx][y+dy] == '1':

                            q.append((x+dx,y+dy))

                            danzi[x+dx][y+dy] = '0'

                            d_cnt+=1

            d_lst.append(d_cnt)

d_lst.sort()

print(all_d)

for d in d_lst:

    print(d)