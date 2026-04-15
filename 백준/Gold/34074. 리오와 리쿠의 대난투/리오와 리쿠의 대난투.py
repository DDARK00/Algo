import sys
input=sys.stdin.readline

n,m=map(int,input().split())

if n==1 and m==1:
    print(-1)
    exit()

if n>=m:
    # 3 1
    # 12 7 10/3
    # 3
    # 1000 10e9 
    for i in range(1,n):
        print(i, end=" ")
    print(1000000000)

    for i in range(n, n+m):
        print(i, end=" ")
    print()
else:
    a=[]
    b=[]
    # n<m
    if n==1 and m==2:
        print(3)
        print(1, 4)
    else:
        for i in range(m,n+m):
            print(i, end=" ")
        print()
        for i in range(1,m):
            print(i, end=" ")
        print(1000000000)