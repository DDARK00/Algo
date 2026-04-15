import sys
input=sys.stdin.readline

w=input().rstrip()
s=input().rstrip()

chk={}
cryp=[]
for c in w:
    if chk.get(c):
        continue
    chk[c]=1
    cryp.append(c)

for i in range(26):
    if chk.get(chr(65+i)):
        continue
    cryp.append(chr(65+i))

answer=[]
for c in s:
    answer.append(cryp[ord(c)-65])

print(*answer, sep="")