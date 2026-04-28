import sys
from collections import deque, defaultdict
input=sys.stdin.readline

n=int(input()) # 1<=n<=3
scvs=tuple(map(int,input().split()))
q=deque([scvs])
visited=defaultdict(int)

p=[] # 수제 permutation, maximum 6
t=[]
chk=[0]*n
def dfs(k):
    if k==n:
        p.append(tuple(t))
        return
    for i in range(n):
        if chk[i]:continue
        chk[i]=1
        t.append(i)
        dfs(k+1)
        t.pop()
        chk[i]=0
dfs(0)
del t, chk
visited[scvs]=0
dmg=[9,3,1]
while q:
    scvs=q.popleft() # max 60 60 60
    # cushion bounce 9 3 1
    for k in p:
        tmp=[]
        for i, no in enumerate(k):
            tmp.append(max(0,scvs[no]-dmg[i]))
        nxt=tuple(tmp)
        if visited[nxt]:continue
        if sum(nxt)==0:
            print(visited[scvs]+1)
            exit()
        visited[nxt]=visited[scvs]+1
        q.append(nxt)