import sys

from collections import deque

input = sys.stdin.readline

t = int(input())

# 0<ij<9 아니 쌩노가다네

def chkway(direction, i, j,mcnt, route):

    if direction == 1:

        # i j + +

        for k in range(1,8):

            if i+k<9 and j+k<9:

                if not visited.get((i+k,j+k)):

                    eng = f'{route} {change[i+k]} {j+k}'

                    q.append((i+k,j+k,mcnt+1,eng))

            else:

                break

        

    elif direction == 2:

        # i j + -

        for k in range(1,8):

            if i+k<9 and j-k>0:

                if not visited.get((i+k,j-k)):

                    eng = f'{route} {change[i+k]} {j-k}'

                    q.append((i+k,j-k,mcnt+1,eng))

            else:

                break

    elif direction == 3:

        for k in range(1,8):

            if i-k>0 and j-k>0:

                if not visited.get((i-k,j-k)):

                    eng = f'{route} {change[i-k]} {j-k}'

                    q.append((i-k, j-k,mcnt+1,eng))

            else:

                break

        # i j - -

        

    else:

        # i j - +

        for k in range(1,8):

            if i-k>0 and j+k<9:

                if not visited.get((i-k, j+k)):

                    eng = f'{route} {change[i-k]} {j+k}'

                    q.append((i-k,j+k,mcnt+1,eng))

            else:

                break

        

    

    

for _ in range(t):

    

    lst = input().split()

    # 시작 도착

    # A B C D E F G H

    # 1 2 3 4 5 6 7 8

    # 행 M 가로 

    change = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,

             1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H'}

    start = (change[lst[0]], int(lst[1]),0,f'{lst[0]} {lst[1]}')

    # 현재 좌표, 움직인 수, 경로

    end = (change[lst[2]], int(lst[3]))

    # print(start,end)

    # 홀수끼리 짝수끼리만 이동

    if (start[1]+start[0])%2 !=(end[0]+end[1])%2:

        print("Impossible")

    else:

        #bfs

        #최대 4번 움직일 수 있음

        # 1에서 8까지 0<d<9

        q = deque([start])

        visited = {}

        while q:

            x,y,c,path= q.popleft()

            

            if x == end[0] and y == end[1]:

                print(c, path)

                break

            elif c>4:

                # 어디에 있든 2번만에가는데???

                print("Impossible")

                break

            # 한번에 가는 양 최대7칸 4방향

            if not visited.get((x,y)):

                visited[(x,y)] = 1

                for i in range(1,5):

                    chkway(i, x, y, c,path)

                    # 상상 상하 하하 하상 하하하하하