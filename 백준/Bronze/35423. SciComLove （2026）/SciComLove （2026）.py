import sys
input=sys.stdin.readline
s=input().rstrip()

xy=[0,0]
for c in s:
    if c=='S':
        xy[0]+=1
    if c=='L':
        xy[1]+=1

print("SciCom"*xy[0],end='')
print("Love"*xy[1])