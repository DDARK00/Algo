from heapq import heappop, heappush
n,m,b=map(int,input().split())

pq=[0]*m
for num in map(int,input().split()):
    v=heappop(pq)
    heappush(pq,v+num)

if pq[0]>b:
    print("GO")
else:
    print("WAIT")