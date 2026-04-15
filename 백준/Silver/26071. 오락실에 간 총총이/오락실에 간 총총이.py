import sys
input=sys.stdin.readline
n=int(input())
lst=[input().rstrip()for _ in range(n)]

i_min, i_max, j_min, j_max=n, 0, n, 0
for i in range(n):
    for j in range(n):
        if lst[i][j]=='G':
            i_min=min(i_min,i)
            i_max=max(i,i_max)
            j_min=min(j_min,j)
            j_max=max(j,j_max)
# 벽까지의 거리
k=i_max-i_min
l=j_max-j_min
m=min(j_min+l,n-j_max-1+l)
n=min(i_min+k,n-1-i_max+k)

if k==0 and l==0:
    print(0)
elif k==0:
    print(m)
elif l==0:
    print(n)
else:
    print(m+n)