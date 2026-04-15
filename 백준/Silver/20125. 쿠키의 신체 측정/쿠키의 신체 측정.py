import sys
input=sys.stdin.readline
n=int(input())
lst=[input().rstrip() for _ in range(n)]

flag=False
for i in range(n):
    for j in range(n):
        if lst[i][j]=='*':
            hi,hj=i+1,j
            flag=True
            break # heart
    if flag:
        break

print(hi+1,hj+1)
for j in range(n):
    if lst[hi][j]=='*':
        print(hj-j,end=' ')
        break

for j in range(n-1,hj,-1):
    if lst[hi][j]=='*':
        print(j-hj,end=' ')
        break

for i in range(hi+1,n):
    if lst[i][hj]=='_':
        print(i-hi-1,end=' ') # w
        for j in range(1,n):
            nx,ny=i+j-1,hj-1
            if nx==n or ny==0 or lst[nx][ny]=='_':
                print(j-1,end=' ')
                break
        for j in range(1,n):
            nx,ny=i+j-1,hj+1
            if nx==n or ny==n or lst[nx][ny]=='_':
                print(j-1)
                break
        break