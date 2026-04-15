import sys
from heapq import heappop as pop, heappush as push
input=sys.stdin.readline

n=int(input())
pq_pos=[]
pq_neg=[]
ans=0
for _ in range(n):
    k=int(input())
    if k==1:
        ans+=1
    elif k>0:
        push(pq_pos,-k)
    else:
        push(pq_neg,k)

while pq_pos:
    k=-pop(pq_pos)
    if pq_pos:
        k*=-pop(pq_pos)
    ans+=k

while pq_neg:
    k=pop(pq_neg)
    if pq_neg:
        k*=pop(pq_neg) # -1 0 -> 0, -1 -1 -> 1, 1 -1 -> 0
    ans+=k
print(ans)