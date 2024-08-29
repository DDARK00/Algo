import sys

input = sys.stdin.readline

n, m = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(n)]

subset = [[0]*(n+1) for _ in range(n+1)]

sums_x = 0

sums_y = 0

for i in range(1,1+n):

    sums_x+=lst[i-1][0]

    sums_y+=lst[0][i-1]

    subset[i][1] = sums_x

    subset[1][i] = sums_y

for i in range(1,n+1):

    for j in range(1,n+1):

        

        subset[i][j] = subset[i-1][j]+subset[i][j-1]+lst[i-1][j-1]-subset[i-1][j-1]

# print(*subset, sep="\n")

for _ in range(m):

    x1,y1,x2,y2 = map(int,input().split())

    # print(x1,y1,x2,y2)

    l = subset[x2][y1-1]

    u = subset[x1-1][y2]

    c = subset[x1-1][y1-1]

    f = subset[x2][y2]

    print(f-u-l+c)

    