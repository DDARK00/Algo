import sys;input=sys.stdin.readline
a,b,c=0,0,0
for _ in range(int(input())):
    d,*e=map(int,input().split())
    if d==1:
        e=e[0]
        a+=1
        if a==b:
            c=min(c,e)
        elif a>b:
            b=a
            c=e
    else:
        a-=1
print(b,c)