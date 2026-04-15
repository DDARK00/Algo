import sys
input=sys.stdin.readline
n,m=map(int,input().split())

lst=[list(map(int,input().split())) for _ in range(n)]

answer=0
for i in range(m):
    for j in range(i+1,m):
        for k in range(j+1,m):
            tmp=0
            for l in range(n):
                tmp+=max([lst[l][i],lst[l][j],lst[l][k]])
            answer=max(answer,tmp)
print(answer)