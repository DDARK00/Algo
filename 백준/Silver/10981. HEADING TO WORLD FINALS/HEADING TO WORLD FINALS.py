import sys
input=sys.stdin.readline
n,k=map(int,input().split())
p={}
for i,m in enumerate(sorted([input().split() for _ in range(n)],key=lambda x:(-int(x[2]),int(x[3])))):
    if p.get(m[0]):continue
    if len(p)==k:break
    p[m[0]]=1
    print(m[1])