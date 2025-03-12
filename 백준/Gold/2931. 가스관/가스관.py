import sys
input=sys.stdin.readline

r, c = map(int, input().split())

city = [input().rstrip() for _ in range(r)]
tile = ['|','-','+','1','2','3','4']

delta = [(-1,0),(1,0),(0,-1),(0,1)] # u d l r

checker = [
    [tile[0], tile[2], tile[3], tile[6]], # u
    [tile[0], tile[2], tile[4], tile[5]], # d
    [tile[1], tile[2], tile[3], tile[4]], # l
    [tile[1], tile[2], tile[5], tile[6]] # r
]

ans = {15:tile[2], 12:tile[1],10:tile[3],9:tile[4],6:tile[6],5:tile[5],3:tile[0]}
def search(x, y):
    if city[x][y] == ".":
        chk = [0]*4
        find = False
        for i in range(4):
            nx, ny = x+delta[i][0], y+delta[i][1]
            if 0<=nx<r and 0<=ny<c and city[nx][ny] != ".":
                if city[nx][ny] in checker[i]:
                    chk[i] = 1
                    find = True
        if find:
            rst = 0
            for i in range(4):
                rst += chk[i]<<i
            # print(chk, ans, rst)
            print(x+1, y+1, ans[rst])
            return True
    else:
        return False

for i in range(r):
    for j in range(c):
        if search(i, j):
            break
