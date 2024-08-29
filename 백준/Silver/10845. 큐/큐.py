import sys

from collections import deque

input = sys.stdin.readline

n= int(input())

# 오더 수

q = deque([])

for _ in range(n):

    order, *k = input().split()

    

    # print(order, k)

    if order == 'push':

        q.append(k[0])

    elif order == 'pop':

        if q:

            print(q.popleft())

        else:

            print(-1)

    elif order =='front':

        if q:

            print(q[0])

        else:

            print(-1)

    elif order == 'back':

        if q:

            print(q[-1])

        else:

            print(-1)

    elif order == 'size':

        print(len(q))

    elif order == 'empty':

        if q:

            print(0)

        else:

            print(1)