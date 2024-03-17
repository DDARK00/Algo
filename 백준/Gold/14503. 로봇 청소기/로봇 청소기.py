import sys

input = sys.stdin.readline

n, m = map(int,input().split())

#높이 너비

r, c, d = map(int,input().split())

# 좌표, 방향

room = [input().split() for _ in range(n)]

# 방 배열

# 0청소할거 1벽

clean = 0

def moving(x,y,dir):

    # print(x,y)

    global clean

    

    if room[x][y] =="0":

        room[x][y] = "3"

        clean+=1

    delta = [(-1,0),(0,1),(1,0),(0,-1)]

    # 탐색

    find =False

    for dx, dy in delta:

        nx = x+dx

        ny = y+dy

        if 0<=nx<n and 0<=ny<m and room[nx][ny]=="0":

            find = True

            break

    

    if find:

        # 찾았으면 -90도 돌기+앞이 청소x면 전진

        # 동1->북0 북0->서3 서3->남2 남2->동1

        for _ in range(4):

            

            dir = (dir+4-1)%4

            fx,fy = delta[dir]

            if 0<=x+fx<n and 0<=y+fy<m and room[x+fx][y+fy] =="0":

                return x+fx, y+fy, dir

                

    else:

        # 못찾았으면 1보후퇴

        # 동1<-> 서3 남2<->북0

        bx,by = delta[dir-2]

        if room[x+bx][y+by]!="1":

            return x+bx,y+by,dir

        else:

            return x,y,dir

            # 뒤가 벽이면 종료

    

# 0북 1동 2남 3서

while True:

    nr,nc, nd = moving(r, c, d)

    if nr == r and nc == c:

        break

    else:

        r = nr

        c = nc

        d = nd

    # 같은 좌표가 나오면 종료

print(clean)

# print(*room, sep="\n")