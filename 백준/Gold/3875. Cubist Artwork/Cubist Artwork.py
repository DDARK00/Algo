import sys

input = sys.stdin.readline

while True:

    a, b = map(int,input().split())

    if a==0 and b==0:

        break

    ba = list(map(int,input().split()))

    bb = list(map(int,input().split()))

    ans = 0

    for el in ba:

        ans+=el

        for i in range(len(bb)):

            if el == bb[i]:

                bb[i] = 0

                break

    ans+=sum(bb)

    print(ans)

        