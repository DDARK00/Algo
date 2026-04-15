import sys
input=sys.stdin.readline
a=[0,0,0,0]
for _ in range(int(input())):
    x,y=map(int,input().split())
    a[x>y]+=1
    a[(x<y)+2]+=1
print(a[1],a[3])