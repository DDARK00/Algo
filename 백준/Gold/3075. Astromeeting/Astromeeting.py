import sys
input=sys.stdin.readline

# t100 n100 p100 n^3 1000000+p*n
for _ in range(int(input())):
    n,p,q=map(int,input().split())

    target=[int(input()) for _ in range(n)]

    dist=[[float('inf')]*(p+1) for _ in range(p+1)]
    for i in range(1,p+1):
        dist[i][i]=0
    for _ in range(q):
        i,j,d=map(int,input().split())
        dist[i][j]=min(d,dist[i][j])
        dist[j][i]=min(d,dist[j][i])

    for m in range(1,p+1):
        for s in range(1,p+1):
            if dist[s][m]==float('inf'):continue
            for e in range(1,p+1):
                if dist[m][e]==float('inf'):continue
                if dist[s][m]+dist[m][e]<dist[s][e]:
                    dist[s][e]=dist[s][m]+dist[m][e]

    ans=[float('inf'),float('inf')] # v, cost
    for i in range(1,p+1):
        tmp=0
        for v in target:
            if dist[i][v]==float('inf'):
                tmp=float('inf')
                break
            tmp+=dist[i][v]**2
        if tmp<ans[1]:
            ans=[i,tmp]
    print(*ans)