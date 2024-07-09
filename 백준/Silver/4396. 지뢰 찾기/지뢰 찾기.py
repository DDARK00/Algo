import sys
input = sys.stdin.readline
n=int(input())

bom = [input().rstrip() for _ in range(n)]
lst=[input().rstrip()for _ in range(n)]

delta = [(0,1),(0,-1),(1,-1),(1,1),(-1,-1),(-1,1),(1,0),(-1,0)]
hit = False
ans = []
for i in range(n):
    line = ""
    for j in range(n):
        if lst[i][j]=="x":
            if bom[i][j] == "*":
                hit = True
            cnt=0
            for dx, dy in delta:
                nx, ny = i+dx,j+dy
                if 0<=nx<n and 0<=ny<n and bom[nx][ny]=="*":
                    cnt+=1
            line+=str(cnt)
        else:
            line+="."
    ans.append((list(line)))
if hit:
    for i in range(n):
        for j in range(n):
            if bom[i][j] == "*":
                ans[i][j] = "*"
list(map(print,map("".join,ans)))