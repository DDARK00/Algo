import sys
from math import ceil
from heapq import heappop, heappush

input = sys.stdin.readline

TC = int(input())


def swap(k):
    while k > 1 and -mx[0] > mn[0]:
        tx, ty = heappop(mx), heappop(mn)
        heappush(mx, -ty)
        heappush(mn, -tx)


for _ in range(TC):
    n = int(input())
    lst = []
    for i in range(ceil(n / 10)):
        lst.extend(list(map(int, input().split())))
    # 홀수개니까 최대에 넣고 가장 큰 것
    mx = []  # 최대힙
    mn = []  # 최소힙
    arr = []
    print(ceil(n / 2))
    for i in range(1, n + 1):
        if i % 2 == 1:  # 짝수일때
            heappush(mx, -lst[i - 1])
            swap(i - 1)
            print(-mx[0], end=" ")
        else:  # 홀수일때
            heappush(mn, lst[i - 1])
            swap(i - 1)
        if i % 20 == 0:
            print()
    print()
