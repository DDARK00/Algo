import sys
input=sys.stdin.readline
n,k=map(int,input().split())
co=[[0,[-1,-1,-1]]]
for _ in range(n):
    p,*q=map(int,input().split())
    co.append([p,q])
co.sort(key=lambda x:(-x[1][0],-x[1][1],-x[1][2]))

for i in range(n):
    if co[i][0]==k:
        j=i
        while co[i][1]==co[j-1][1]:
            j-=1
        print(j+1)
        break