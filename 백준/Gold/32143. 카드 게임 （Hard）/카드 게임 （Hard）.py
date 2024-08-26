import sys
from heapq import heappop, heappush
input = sys.stdin.readline

h = int(input())
n, q = map(int, input().split())
# cards query

lst = list(map(int,input().split()))
pq = []
attack = 0
lst.sort(reverse=True)

for num in lst:
    if attack<h:
        attack+=num
        heappush(pq,num)
        pass
    else:
        break

if attack>=h:
    print(len(pq))
else:
    print(-1)

for _ in range(q):
    num = int(input())
    if attack<h or (pq and pq[0]<num):
        attack+=num
        heappush(pq,num)

    while pq and attack-pq[0]>h:
        attack-=pq[0]
        heappop(pq)

    if attack>=h:
        print(len(pq))
    else:
        print(-1)