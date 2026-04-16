import sys
input=sys.stdin.readline

chk={}
d=[(-1,-2),(-1,2),(1,-2),(1,2),(-2,-1),(-2,1),(2,-1),(2,1)]
for i in range(1,7):
    for j in range(1,7):
        chk[(i,j)]=0

s=input().rstrip()
change={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6}

st=(change[s[0]],int(s[1])) # (i,j)
bf=st
chk[st]+=1

for _ in range (35):
    s=input().rstrip()
    i,j=change[s[0]],int(s[1])
    ok=False
    for dx,dy in d:
        nx,ny=bf[0]+dx,bf[1]+dy
        if nx==i and ny==j:
            ok=True
            break
    if ok:
        bf=(i,j)
        chk[bf]+=1
    else:
        print('Invalid')
        exit(0)

ok=False
for dx,dy in d:
    nx,ny=bf[0]+dx,bf[1]+dy
    if nx==st[0] and ny==st[1]:
        ok=True
        break

if ok:
    for _,v in chk.items():
        if v!=1:
            ok=False
            break
if ok:
    print('Valid')
else:
    print('Invalid')