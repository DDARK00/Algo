import sys
from collections import defaultdict

input = sys.stdin.readline

a, b = map(int, input().split())
ba = [int(input()) for _ in range(a)]
bb = [int(input()) for _ in range(b)]

if max(ba) == max(bb):
    di = defaultdict(int)
    minV = 0
    maxV = 0
    ba.sort(key=lambda x: -x)
    bb.sort(key=lambda x: -x)

    for level in ba:
        di[level] += 1
        minV += level

    for level in range(b - 1, -1, -1):
        di[bb[level]] -= 1
        if di[bb[level]] < 0:
            minV += bb[level]
    while ba and ba[-1] == 0:
        ba.pop()
    while bb and bb[-1] == 0:
        bb.pop()
    if ba and bb :
        for level in range(1, max(ba) + 1):
            maxV += len(ba) * len(bb)
            while ba and ba[-1] == level:
                ba.pop()
            while bb and bb[-1] == level:
                bb.pop()

    print(minV, maxV)
else:
    print(-1)
