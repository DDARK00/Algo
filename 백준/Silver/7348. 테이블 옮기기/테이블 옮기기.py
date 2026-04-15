from heapq import heappop, heappush
for _ in range(int(input())):
    pq=[]
    answer=0
    for s, t in sorted([tuple(sorted(map(int,input().split())))for _ in range(int(input()))]):
        s,t=(s-1)//2,(t-1)//2
        while pq and pq[0]<s:
            heappop(pq)
        heappush(pq, t)
        answer=max(answer,len(pq)*10)
    print(answer)