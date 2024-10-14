import sys

from collections import defaultdict

input=sys.stdin.readline

n, m = map(int, input().split())

g = defaultdict(list)

chk = [0]*(n+1)

for _ in range(m):

    lst = list(map(int, input().split()))

    for i in range(1, len(lst)-1):

        a = lst[i]

        b = lst[i+1]

        chk[b]+=1

        g[a].append(b)

ans = []

st = []

def d(t):

    ans.append(t)

    for num in g[t]:

        chk[num]-=1

        if chk[num] == 0:

            chk[num] = -1

            d(num)

for i in range(1, n+1):

    if chk[i] == 0:

        chk[i] = -1

        d(i)

if len(ans) != n:

    print(0)

else:

    print(*ans, sep="\n")