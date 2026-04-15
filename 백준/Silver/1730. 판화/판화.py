import sys
input=sys.stdin.readline

n=int(input())

board = [["." for _ in range(n)] for _ in range(n)]


g = {
    "D":(1,0),
    "R":(0,1),
    "U":(-1,0),
    "L":(0,-1)
}

cmd = input().rstrip()
x=0
y=0

edit = {
    "U":{
        ".":"|",
        "|":"|",
        "+":"+",
        "-":"+",
    },
    "D":{
        ".":"|",
        "|":"|",
        "+":"+",
        "-":"+",
    },
    "R":{
        ".":"-",
        "-":"-",
        "+":"+",
        "|":"+",
    },
   "L":{
        ".":"-",
        "-":"-",
        "+":"+",
        "|":"+",
    } 
}
for c in cmd:
    dx, dy = g[c]
    nx, ny = x+dx, y+dy
    if 0<=nx<n and 0<=ny<n:
        board[x][y] = edit[c][board[x][y]]
        board[nx][ny] = edit[c][board[nx][ny]]
        x = nx
        y = ny
print(*map("".join,board), sep="\n")