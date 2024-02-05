from collections import deque
import sys

input = sys.stdin.readline


def R(header):
    header = not header
    return header


def D(arr: deque, header):
    if arr:
        if header:
            arr.popleft()
        else:
            arr.pop()
        return
    else:
        raise Exception


T = int(input())

for t in range(T):
    orders = input()
    n = int(input())
    #  배열
    try:
        in_list = input().strip()[1:-1]

        if in_list:
            in_list = list(in_list.split(","))

        deq = deque(in_list)

        head = True
        # True면 left
        # False면 right

        for order in orders:
            if order == 'R':
                head = R(head)
            elif order == "D":
                D(deq, head)

        if not head:
            deq.reverse()

        deq = ",".join(list(map(str, deq)))
        print('[' + deq + ']')
    except Exception as e:
        print('error')
