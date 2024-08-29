import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [input().rstrip() for _ in range(n)]

ans = 0
for i in range(1,n-1):
    up = 0
    down = 0
    for j in range(1,m-1):
        if lst[i][j] == ".":
            if lst[i-1][j] == "X": # up
                if up == 1:
                    ans+=1
                    up = 0
                else:
                    up = 1
            else:
                up = 0
            if lst[i+1][j] == "X": # down
                if down == 1 :
                    ans+=1
                    down = 0
                else:
                    down =1
            else:
                down = 0
        else:
            up = 0
            down = 0

for i in range(1,m-1):
    left = 0
    right = 0
    for j in range(1,n-1):
        if lst[j][i] == ".":
            if lst[j][i-1] =="X":
                if left == 1:
                    ans+=1
                    left = 0
                else:
                    left = 1
            else:
                left = 0
            if lst[j][i+1] == "X":
                if right == 1:
                    ans+=1
                    right = 0
                else:
                    right=1
            else:
                right = 0
        else:
            left = 0
            right = 0
print(ans)