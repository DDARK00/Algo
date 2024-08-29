import sys

input = sys.stdin.readline

r,c,q = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(r)]

subset = [[0]*(c+1) for _ in range(r+1)]

sums_x = 0

sums_y = 0

for i in range(1,1+r):

    sums_x+=lst[i-1][0]

    subset[i][1] = sums_x

for i in range(1,1+c):

    sums_y+=lst[0][i-1]

    

    subset[1][i] = sums_y

for i in range(1,r+1):

    for j in range(1,c+1):

        

        subset[i][j] = subset[i-1][j]+subset[i][j-1]+lst[i-1][j-1]-subset[i-1][j-1]

# print(*subset, sep="\n")

for _ in range(q):

    x1,y1,x2,y2 = map(int,input().split())

    # print(x1,y1,x2,y2)

    l = subset[x2][y1-1]

    u = subset[x1-1][y2]

    c = subset[x1-1][y1-1]

    f = subset[x2][y2]

    cnt = x2*y2-(x1-1)*y2-x2*(y1-1)+(x1-1)*(y1-1)

    # print(cnt,"cnt")

    print(int((f-u-l+c)/cnt))

    