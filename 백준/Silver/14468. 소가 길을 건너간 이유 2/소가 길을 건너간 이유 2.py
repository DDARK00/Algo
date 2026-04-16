import sys
input=sys.stdin.readline

answer=0
s=input()
chk={}
for idx, c in enumerate(s):
    if chk.get(c):
        continue
    chk[c]=1
    plus=[0]*26
    for i in range(idx+1, 52):
        if s[i]==c:
            answer+=sum(plus)
            break
        plus[ord(s[i])-65] ^=1
print(answer//2)
