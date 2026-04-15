import sys
from collections import defaultdict,deque
input=sys.stdin.readline

n, m = map(int, input().split())
start = input().rstrip()

g=defaultdict(list)
deg=defaultdict(int)

for _ in range(n):
    c, p1, p2 = input().split()
    g[p1].append(c)
    g[p2].append(c)
    deg[c]+=2
blood=defaultdict(int)
blood[start]=1 # n, m <=50

q=deque([])
for k in g.keys():
    if deg[k]==0:
        q.append(k)
        deg[k]=-1

while q:
    v=q.popleft()
    for nv in g[v]:
        deg[nv]-=1
        blood[nv]+= blood[v]/2
        if deg[nv]==0:
            deg[nv]=-1
            q.append(nv)

t_blood = -1
t_name = ""
for _ in range(m):
    if blood[x:=input().rstrip()]>t_blood:
        t_name=x
        t_blood=blood[x]
print(t_name)