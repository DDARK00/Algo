import sys, math

from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input()) # 별자리의 수

stars = [tuple(map(float,input().split())) for _ in range(n)]

# 별의 위치, x, y

g = [[] for _ in range(n)]

for i in range(n):

    x,y = stars[i]

    for j in range(i+1,n):

        p,q = stars[j]

        d = math.sqrt((p-x)**2+(q-y)**2)

        g[i].append((d,j))

        g[j].append((d,i))

    

# MST

# print(g)

def prim(n):

    visit = [0]*n

    k = 0

    dist = 0

    pq = [(0,0)] # w, v start

    

    while True:

        w,v = heappop(pq)

        

        if not visit[v]:

            visit[v] = 1

            dist+=w

            k+=1

            if k == n:

                return dist

            for x in g[v]:

                if not visit[x[1]]:

                    heappush(pq,x)

                

    

    # return dist

print(f'{prim(n):.2f}')

    

    