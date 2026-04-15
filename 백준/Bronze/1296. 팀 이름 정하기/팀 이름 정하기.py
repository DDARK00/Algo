import sys
input=sys.stdin.readline

cnt=[0,0,0,0]
p='LOVE'
s=input().rstrip()
for i in range(4):
    cnt[i]=s.count(p[i])

teams=[]
for _ in range(int(input())):
    s=input().rstrip()
    q=cnt[:]
    for i in range(4):
        q[i]+=s.count(p[i])
    L,O,V,E=q
    k=(((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100)
    teams.append((k,s))

teams.sort(key=lambda x:(-x[0],x[1]))
print(teams[0][1])