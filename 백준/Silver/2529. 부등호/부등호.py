import sys
input=sys.stdin.readline

k=int(input())
signs=input().split()

def issignsright(a,flag,b):
    return a<b if flag=='<' else a>b

lst=[range(9,-1,-1),range(10)]

def solve(d,l):
    if d==k:
        print(*sel,sep='')
        return 1
    for i in lst[l]:
        if not use[i] and issignsright(sel[d],signs[d],i):
            use[i]=1
            sel.append(i)
            if solve(d+1,l):
                return 1
            sel.pop()
            use[i]=0

use=[0]*10
sel=[]
# 9->0 0->9 약간 추상화
for idx, d in enumerate(lst):
    use=[0]*10
    sel=[]
    for i in d:
        use[i]=1
        sel.append(i)
        if solve(0,idx):
            break
        sel.pop()
        use[i]=0