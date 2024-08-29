import sys

from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())

pq = []

for _ in range(n):

    t, d = map(int,input().split())

    heappush(pq,(d,t))

after = []

m = int(input())

for _ in range(m):

    w, t, d = map(int,input().split())

    heappush(after,(w,d,t)) # 추가시간 마감 잔여

now = 0

suc = True

while True:

    if pq:

        d, t = heappop(pq)

        if after and after[0][0]<=now+t:

            w, nd, nt = heappop(after)

            t -= w - now

            now = w

            heappush(pq,(d,t))

            heappush(pq,(nd,nt))

        else:

            now+=t

        if now > d:

            suc = False

            break

    elif after:

        w, d, t = heappop(after)

        if now < w :

            now = w

            heappush(pq,(d,t))

        else:

            suc = False

            break

    else:

        break

if suc:

    print('YES')

    print(now)

else:

    print('NO')