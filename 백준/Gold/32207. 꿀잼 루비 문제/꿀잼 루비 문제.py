import sys
from collections import defaultdict
input=sys.stdin.readline

n,m,k=map(int,input().split())

ruby=[]
for i in range(n):
    for j, v in enumerate(map(int,input().split())):
        ruby.append((v,i,j))
# 1 9 1 1 1
# 9 21 9 5 1
# 1 9 5 8 5
# 1 1 1 5 1
# 1 1 1 1 1
# k=5 44
# k=2 29
ruby=sorted(ruby,key=lambda x:-x[0])[:min((k-1)*5+1,n*m)]

chk=defaultdict(int)
answer=0
aa=0
def dfs(idx,k,val):
    global answer, aa
    answer=max(answer,val)
    if k==0 or idx==len(ruby):
        return
    for i in range(idx,len(ruby)):
        tv, tx, ty=ruby[i]
        ok=True
        for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            if chk[(tx+dx,ty+dy)]:
                ok=False
                break
        if ok:
            chk[(tx,ty)]=1
            dfs(i+1,k-1,val+tv)
            chk[(tx,ty)]=0
        # dfs(i+1,k,val)
    return

dfs(0,k,0)
print(answer)
# k=5 약 6000번