import sys
input=sys.stdin.readline
n=int(input())

dist=[[float('inf')]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    dist[i][i]=0

for _ in range(int(input())):
    a,b=map(int,input().split())
    dist[a][b]=1
    dist[b][a]=-1

for m in range(1,n+1):
    for s in range(1,n+1):
        for e in range(1,n+1):
            # ab+ bc+ -> ac+
            # ab- bc- -> ac-
            if dist[s][m]==1 and dist[m][e]==1:
                dist[s][e]=1
            elif dist[s][m]==-1 and dist[m][e]==-1:
                dist[s][e]=-1
# print(*dist,sep='\n')

for i in range(1,n+1):
    print(dist[i].count(float('inf'))-1)