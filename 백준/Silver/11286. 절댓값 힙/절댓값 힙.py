import sys

from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())

hq = []

for _ in range(n):

    k = int(input())

    if k == 0:

        if hq:

            val, o = heappop(hq)

            if o:

                print(val)

            else:

                print(-val)

        else: 

            print(0)

    else:

        oper = 1 if k>0 else 0

        heappush(hq,(abs(k), oper))