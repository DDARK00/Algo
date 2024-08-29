import sys

input = sys.stdin.readline

n = int(input())

a, b, c = [[0,0,0,0,1],[0,0,0,0,2],[0,0,0,0,3]]

# sum 1 2 3 idx

for _ in range(n):

    x, y, z = map(int,input().split())

    a[0]+=x

    a[x]+=1

    b[0]+=y

    b[y]+=1

    c[0]+=z

    c[z]+=1

    

rank = sorted([a,b,c], key= lambda x:(-x[0],-x[3],-x[2]))

if rank[0][0]==rank[1][0] and rank[0][3]==rank[1][3]and rank[0][2]==rank[1][2]:

    print(f'0 {rank[0][0]}')

else:

    print(f'{rank[0][4]} {rank[0][0]}')