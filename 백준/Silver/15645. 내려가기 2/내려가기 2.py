import sys
input=sys.stdin.readline

n=int(input())
a,b,c=map(int,input().split())
mx=[a,b,c]
mn=[a,b,c]
tmp=[0,0,0]
for i in range(1,n):
    a,b,c=map(int,input().split())
    tmp[0]=max(mx[0],mx[1])+a
    tmp[1]=max(mx)+b
    tmp[2]=max(mx[1],mx[2])+c
    mx[0],mx[1],mx[2]=tmp[0],tmp[1],tmp[2]

    tmp[0]=min(mn[0],mn[1])+a
    tmp[1]=min(mn)+b
    tmp[2]=min(mn[1],mn[2])+c
    mn[0],mn[1],mn[2]=tmp[0],tmp[1],tmp[2]
print(max(mx),min(mn))