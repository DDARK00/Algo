n=int(input())
x,y=map(int,input().split())
a=0
for i,j in[(0,1),(0,-1),(1,0),(-1,0)]:
    k,l=x+i,y+j
    if 0<k<=n and 0<l<=n:
        a+=1
print(a)