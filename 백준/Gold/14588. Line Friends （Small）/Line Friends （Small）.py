import sys
input=sys.stdin.readline
n=int(input())
line=[tuple(map(int,input().split())) for _ in range(n)]

answer=[[float('inf')]*(n+1) for _ in range(n+1)]

for i in range(n):
    a,b=line[i]
    answer[i+1][i+1]=0
    for j in range(i+1, n):
        c,d=line[j]
        if max(a,c)<=min(b,d):
            answer[i+1][j+1]=1
            answer[j+1][i+1]=1

for md in range(1,n+1):
    for st in range(1,n+1):
        for ed in range(1,n+1):
            if answer[st][ed]>answer[st][md]+answer[md][ed]:
                answer[st][ed]=answer[st][md]+answer[md][ed]

for _ in range(int(input())):
    x,y=map(int,input().split())
    print(answer[x][y] if answer[x][y]!=float('inf') else -1)