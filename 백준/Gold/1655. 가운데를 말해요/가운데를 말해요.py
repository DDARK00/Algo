from heapq import heappop, heappush
import sys

input = sys.stdin.readline

n = int(input())

mxhp = []

mnhp = []
# test = []
for i in range(n):
    k = int(input())
    if len(mxhp) > len(mnhp):
        heappush(mnhp, k)
    else:
        heappush(mxhp, -k)

    min_head = None
    max_head = -mxhp[0]
    if mnhp:
        min_head = mnhp[0]
    while min_head is not None and max_head > min_head:
        mx = heappop(mxhp)
        mn = heappop(mnhp)
        heappush(mxhp, -mn)
        heappush(mnhp, -mx)
        max_head = -mxhp[0]
        min_head = mnhp[0]
    print(max_head)
    # test.append(k)
    # test.sort()
    # print(test)
    # print()

#
'''
6
-1
9
44
13
-15
0
'''
