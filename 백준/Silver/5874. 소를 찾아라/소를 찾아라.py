import sys
input=sys.stdin.readline

s=input()+"."
ans=0
l=0
t=0
u=0
for c in s:
    if c=="(":
        t+=1
    else:
        if t>1:
            l+=t-1
        t=0

    if c==")":
        u+=1
    else:
        if u>1:
            ans+= l*(u-1)
        u=0
print(ans)