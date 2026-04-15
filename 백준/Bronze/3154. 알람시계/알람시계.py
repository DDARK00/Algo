hh,mm=map(int,input().split(":"))

answer=20 # 1010+4
_=None
pos=[(3,1),(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
o=[hh,mm]

def calc(a,b):
    return abs(pos[a][0]-pos[b][0])+abs(pos[a][1]-pos[b][1])

for i in range(hh, 100, 24):
    for j in range(mm, 100, 60):
        tmp=0
        p,q,r,s=i//10,i%10,j//10,j%10
        tmp+=calc(p,q)+calc(q,r)+calc(r,s)
        if tmp<answer:
            answer=tmp
            o=[i,j]
print(*map(lambda x:(("0"+str(x))[-2:]),o),sep=':')