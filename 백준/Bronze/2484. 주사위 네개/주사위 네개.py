import sys
input=sys.stdin.readline
ans=0
for _ in range(int(input())):
    a,b,c,d=sorted(map(int,input().split()))
    s={a,b,c,d}
    if len(s)==1:
        ans=max(50000+a*5000,ans)
    elif len(s)==2:
        if b==c:
            ans=max(10000+b*1000,ans)
        else:
            ans=max(2000+500*(b+c),ans)
    elif len(s)==3:
        t=c
        if a==b:
            t=b
        ans=max(1000+t*100,ans)
    else:
        ans=max(d*100,ans)
print(ans)