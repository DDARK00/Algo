from collections import deque

'''
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''


def push(x, queue: deque):
    queue.append(x)
    return


def pops(queue: deque):
    if queue:
        print(queue.popleft())
        return
    else:
        print(-1)
        return


def sizes(queue: deque):
    print(len(queue))
    return


def empty(queue: deque):
    if queue:
        print(0)
        return
    else:
        print(1)
        return


def front(queue: deque):
    if queue:
        print(queue[0])
        return
    else:
        print(-1)
        return


def back(queue: deque):
    if queue:
        print(queue[-1])
        return
    else:
        print(-1)
        return -1


import sys

input = sys.stdin.readline

deq = deque()

n = int(input())
for i in range(n):
    order: str = input().strip()
    x = 0
    if order.startswith(('push')):
        order, x = order.split()
        push(x, deq)
    elif order == 'pop':
        pops(deq)
    elif order == 'size':
        sizes(deq)
    elif order == 'empty':
        empty(deq)
    elif order == 'front':
        front(deq)
    elif order == 'back':
        back(deq)
