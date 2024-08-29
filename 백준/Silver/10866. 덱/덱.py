import sys

from collections import deque

input = sys.stdin.readline

n = int(input())

# 명령의 수

deq = deque([])

for _ in range(n):

    order, *k = input().split()

    if order == "push_back":

        deq.append(k[0])

    elif order == "push_front":

        deq.appendleft(k[0])

    elif order == "front":

        if deq:

            print(deq[0])

        else:

            print(-1)

    elif order == "back":

        if deq :

            print(deq[-1])

        else:

            print(-1)

    elif order == "size":

        print(len(deq))

    elif order == "empty":

        if not deq :

            print(1)

        else:

            print(0)

    elif order == "pop_front":

        if deq:

            print(deq.popleft())

        else:

            print(-1)

    elif order == "pop_back":

        if deq:

            print(deq.pop())

        else:

            print(-1)

