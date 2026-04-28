import sys
input=sys.stdin.readline
n,l,r,x=map(int,input().split())

ans=0
sums=0
sel=[]
lst=list(sorted(map(int,input().split())))
def dfs(k): # depth
    global ans, sums
    if sums>r:
        return
    if len(sel)>1 and sums>=l and sel[-1]-sel[0]>=x:
        ans+=1

    for i in range(k,n):
        sel.append(lst[i])
        sums+=lst[i]
        dfs(i+1)
        sel.pop()
        sums-=lst[i]

dfs(0)

print(ans)