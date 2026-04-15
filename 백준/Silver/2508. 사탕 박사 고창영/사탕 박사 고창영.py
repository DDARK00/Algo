import sys
input=sys.stdin.readline

for _ in range(int(input())):
    input()
    r, c=map(int,input().split())
    lst=[input().rstrip()for _ in range(r)]

    ans=0
    for i in range(r):
        for j in range(c):
            if lst[i][j]=='>':
                if j+2<c and lst[i][j+1]=='o'and lst[i][j+2]=='<':
                    ans+=1
            if lst[i][j]=='v':
                if i+2<r and lst[i+1][j]=='o'and lst[i+2][j]=='^':
                    ans+=1
    print(ans)