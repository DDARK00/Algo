import sys
input=sys.stdin.readline

s, k=input().split()
s+="?"
k=int(k)
chk={}
answer=[]
before=[str.lower(s[0]),0]

for c in s:
    c=str.lower(c)
    if chk.get(c):
        continue
    if before[0]!=c:
        if before[1]<k:
            answer.append(0)
        else:
            answer.append(1)
        chk[before[0]]=1
        before[0]=c
        before[1]=1
    else:
        before[1]+=1

print(*answer,sep="")