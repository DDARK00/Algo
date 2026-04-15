import sys
input=sys.stdin.readline

n,m=map(int,input().split())
chk=[0]*7
data={
    ".":0,"#":1,"U":2,"D":2,"R":2,"L":2,"A":3,"V":4,"S":5,"E":6
}
for _ in range(n):
    for c in input().rstrip():
        chk[data[c]]+=1

if chk[5]!=1 or chk[6]!=1: # S E
    print(-1)
    exit()

if chk[3]>0: # A
    print(4)
    exit()

if chk[4]>0: # V
    print(3)
    exit()

if chk[1]>1 or chk[2]>1: # udlr #
    print(2)
    exit()

print(1)