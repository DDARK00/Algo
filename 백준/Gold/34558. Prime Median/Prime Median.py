import sys
input=sys.stdin.readline

field=[1]*(1000001)

for i in range(2,int(1000001**0.5)):
    if field[i]:
        for j in range(i+i,1000001,i):
            field[j]=0
db={}
chk=[0]*(1000001)
db[0]=0

for i in range(2,1000001):
    chk[i]=chk[i-1]
    if field[i]:
        chk[i]+=1
        db[chk[i]]=i

# chk n까지의소수
# db n번째소수

for _ in range(int(input())):
    a,b=map(int,input().split())
    cnt=chk[b]-chk[a-1]
    if cnt==0 or cnt%2==0:
        print(-1)
        continue
    print(db[chk[b]-(cnt//2)])