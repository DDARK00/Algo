import sys

from heapq import heappush, heappop

input=sys.stdin.readline

T = int(input())

def find_value(pq):

    while pq:

        value,idx = heappop(pq)

        if used[idx]:

            used[idx] = 0

            return value

            

for tc in range(T):

    max_pq = []

    min_pq = []

    q = int(input()) #quert cnt

    used = [1]*q

    for i in range(q):

        order, n = input().split()

        # print(order,n)

        if order == "I": #insert

            n = int(n)

            heappush(max_pq,(-n,i))

            heappush(min_pq,(n,i))

        elif n == "-1": # delete min

            if min_pq:

                find_value(min_pq)

        else: # delete max_pq

            if max_pq:

                find_value(max_pq)

    mx_v = find_value(max_pq)

    mn_v = find_value(min_pq)

    

    if mx_v is not None and mn_v is None:

        print(-mx_v, -mx_v)

    elif mx_v is not None and mn_v is not None:

        print(-mx_v,mn_v)

    else:

        print("EMPTY")